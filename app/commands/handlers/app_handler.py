import subprocess
from app.config.apps import APPS


class AppHandler:

    @staticmethod
    def open_app(data):

        name = data.get("name")

        path = APPS.get(name)

        if not path:
            return f"{name} not installed or not configured"

        subprocess.Popen(path)

        return f"Opening {name}"