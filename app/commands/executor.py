from app.automations.apps import AppOpener
from app.automations.web import WebController
from app.automations.system import SystemController
from app.automations.files import FileController
from app.automations.system import SystemController
import random


class CommandExecutor:

    @staticmethod
    def execute(data):

        intent = data.get("intent")
        

        if intent == "open_chrome":
            AppOpener.open_chrome()
            return "Opening Chrome"

        elif intent == "open_youtube":
            WebController.open_youtube()
            return "Opening YouTube"

        elif intent == "google_search":
            query = data.get("query")
            WebController.search_google(query)

            return f"Searching Google for {query}"

        elif intent == "shutdown":

            messages = [
                "Bohat tez ho rahe ho 😏 shutdown kar ke mujhe bhi band kar do",
                "Theek hai boss... system band kar raha hoon 😄",
                "Shutdown mode on... phir milte hain 👋",
            ]
            return {
            "message": random.choice(messages),
             "action": "shutdown"
             }

        elif intent == "restart":
            return "Restarting computer"
        
        elif intent == "open_project":

            project_name = data.get("project_name")

            success = FileController.open_project(project_name)

            if success:
                return f"Opening project {project_name}"

            return "Project not found"

        elif intent == "exit":
            return "Goodbye"

        return "I did not understand the command"