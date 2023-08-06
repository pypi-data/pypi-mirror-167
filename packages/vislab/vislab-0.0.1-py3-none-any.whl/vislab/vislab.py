import logging
import os
import shutil
import tempfile
from threading import Thread

import numpy as np
import trimesh
from flask import Flask, send_file, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO

DATA_TYPES = ["mesh", "point_cloud", "urdf"]
DATA_DIRS = {"mesh": "meshes", "point_cloud": "point_clouds", "urdf": "urdfs"}
FILE_EXTS = {"mesh": "ply", "point_cloud": "ply", "urdf": "urdf"}

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")


class WebViewer:
    def __init__(self, port=8080, host="localhost", daemon=True, verbose=False):
        self.port = port
        self.host = host
        self.verbose = verbose

        self.cache_dir = tempfile.TemporaryDirectory()
        self.counters = {data_type: 0 for data_type in DATA_TYPES}

        self.scene_meta = {"meshes": [], "point_clouds": [], "urdfs": []}

        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*")
        CORS(self.app, resources={r"/*": {"origins": "*"}})

        log = logging.getLogger("werkzeug")
        log.setLevel(logging.ERROR)

        self.app.add_url_rule("/file/<data_type>/<file_name>", "handle_file", self._handle_file)
        self.app.add_url_rule("/", "handle_index", lambda: send_from_directory(STATIC_DIR, "index.html"))
        self.app.add_url_rule(
            "/manifest.json", "handle_manifest", lambda: send_from_directory(STATIC_DIR, "manifest.json")
        )
        self.app.add_url_rule("/favicon.ico", "handle_favicon", lambda: send_from_directory(STATIC_DIR, "favicon.ico"))
        self.app.add_url_rule("/logo192.png", "handle_logo192", lambda: send_from_directory(STATIC_DIR, "logo192.png"))
        self.app.add_url_rule(
            "/static/<path:path>", "handle_static", lambda path: send_from_directory(STATIC_DIR, path)
        )

        self.socketio.on_event("connect", self._handle_connect)
        self.socketio.on_event("disconnect", self._handle_disconnect)

        def launch_app():
            print(f"WebViewer running on http://{self.host}:{self.port}")
            self.socketio.run(self.app, port=self.port, host=self.host)

        if daemon:
            thread = Thread(target=launch_app, daemon=True)
            thread.start()
        else:
            launch_app()

    def _get_export_file_path(self, data_type, name=None, return_name=True):
        assert data_type in DATA_TYPES, f"Invalid data type: {data_type}"
        if name is None:
            name = f"{self.counters[data_type]:05d}"
            self.counters[data_type] += 1
        file_path = os.path.join(self.cache_dir.name, DATA_DIRS[data_type], f"{name}.{FILE_EXTS[data_type]}")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if return_name:
            return file_path, name
        else:
            return file_path

    def _get_file_url(self, data_type, file_name):
        return f"http://{self.host}:{self.port}/file/{data_type}/{file_name}"

    def _handle_connect(self):
        if self.verbose:
            print("Client connected")
        self._emit_scene()

    def _handle_disconnect(self):
        if self.verbose:
            print("Client disconnected")

    def _handle_file(self, data_type, file_name):
        file_path = self._get_export_file_path(data_type, file_name, return_name=False)
        if self.verbose:
            print(f"Sending file {file_path}")
        return send_file(file_path)

    def _emit_scene(self):
        if self.verbose:
            print("Emitting scene")
        self.socketio.emit("scene", self.scene_meta, broadcast=True)

    def close(self):
        self.cache_dir.cleanup()

    def add_mesh(
        self,
        mesh_or_vertices,
        faces=None,
        vertex_colors=None,
        position=None,
        quaternion=None,
        name=None,
        return_name=False,
    ):
        if isinstance(mesh_or_vertices, str):
            mesh = trimesh.load(mesh_or_vertices)
        elif isinstance(mesh_or_vertices, trimesh.Trimesh):
            mesh = mesh_or_vertices.copy()
        elif isinstance(mesh_or_vertices, np.ndarray):
            mesh = trimesh.Trimesh(vertices=mesh_or_vertices, faces=faces, vertex_colors=vertex_colors)
        else:
            raise ValueError("Invalid mesh type")

        file_path, name = self._get_export_file_path("mesh", name, return_name=True)
        mesh.export(file_path)
        if self.verbose:
            print(f"Exported mesh to {file_path}")

        file_url = self._get_file_url("mesh", name)

        position = position or [0, 0, 0]
        quaternion = quaternion or [0, 0, 0, 1]
        assert isinstance(position, list) and len(position) == 3, "Invalid position type"
        assert isinstance(quaternion, list) and len(quaternion) == 4, "Invalid quaternion type"

        self.scene_meta["meshes"].append(
            {"name": name, "url": file_url, "position": position, "quaternion": quaternion}
        )
        self._emit_scene()

        if return_name:
            return name

    def add_urdf(self, urdf_path, position=None, quaternion=None, joint_values=None, name=None, return_name=False):
        file_path, name = self._get_export_file_path("urdf", name, return_name=True)

        shutil.copyfile(urdf_path, file_path)

        if self.verbose:
            print(f"Exported URDF to {file_path}")

        file_url = self._get_file_url("urdf", name)

        joint_values = joint_values or {}
        assert isinstance(joint_values, dict), "Invalid joint values type"
        position = position or [0, 0, 0]
        quaternion = quaternion or [0, 0, 0, 1]
        assert isinstance(position, list) and len(position) == 3, "Invalid position type"
        assert isinstance(quaternion, list) and len(quaternion) == 4, "Invalid quaternion type"

        self.scene_meta["urdfs"].append(
            {
                "name": name,
                "url": file_url,
                "position": position,
                "quaternion": quaternion,
                "joint_values": joint_values,
            }
        )
        self._emit_scene()

        if return_name:
            return name

    def transform_mesh(self, name, position=None, quaternion=None):
        for mesh in self.scene_meta["meshes"]:
            if mesh["name"] == name:
                if position is not None:
                    assert isinstance(position, list) and len(position) == 3, "Invalid position type"
                    mesh["position"] = position
                if quaternion is not None:
                    assert isinstance(quaternion, list) and len(quaternion) == 4, "Invalid quaternion type"
                    mesh["quaternion"] = quaternion
                break
        else:
            raise ValueError(f"Mesh with name {name} not found")

        self._emit_scene()

    def transform_urdf(self, name, position=None, quaternion=None, joint_values=None):
        for urdf in self.scene_meta["urdfs"]:
            if urdf["name"] == name:
                if position is not None:
                    assert isinstance(position, list) and len(position) == 3, "Invalid position type"
                    urdf["position"] = position
                if quaternion is not None:
                    assert isinstance(quaternion, list) and len(quaternion) == 4, "Invalid quaternion type"
                    urdf["quaternion"] = quaternion
                if joint_values is not None:
                    assert isinstance(joint_values, dict), "Invalid joint values type"
                    urdf["joint_values"] = joint_values
                break
        else:
            raise ValueError(f"URDF with name {name} not found")

        self._emit_scene()


if __name__ == "__main__":
    viewer = WebViewer(verbose=True)
    viewer.close()
