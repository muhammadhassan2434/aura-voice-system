from app.automations.files import FileController


class FileHandler:

    @staticmethod
    def open_project(data):

        project_name = data.get("project_name")

        success = FileController.open_project(project_name)

        if success:
            return f"Opening project {project_name}"

        return "Project not found"