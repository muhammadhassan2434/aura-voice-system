import subprocess
import os
from app.config.projects import PROJECTS

class FileController:

    PROJECTS = {
        "alexa": r"E:\Python\project(alexa)"
    }

    @classmethod
    def open_project(cls, project_name):

        path = PROJECTS.get(project_name)

        print(f"Project: {project_name}")
        print(f"Path: {path}")

        if not path:
            return False

        vscode_path = r"C:\Users\New\AppData\Local\Programs\Microsoft VS Code\Code.exe"

        if os.path.exists(vscode_path):
            subprocess.Popen([vscode_path, path])
        else:
            print("VS Code not found at expected path")

        return True