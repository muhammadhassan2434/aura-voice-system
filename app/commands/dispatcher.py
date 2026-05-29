from app.commands.registry import COMMAND_REGISTRY

class CommandDispatcher:

    @staticmethod
    def dispatch(data):

        actions = data.get("actions", [])

        responses = []

        for action in actions:

            action_type = action.get("type")

            if action_type == "open_youtube":
                from app.commands.handlers.web_handler import WebHandler
                responses.append(WebHandler.open_youtube(action))

            elif action_type == "youtube_search":
                from app.commands.handlers.web_handler import WebHandler
                responses.append(WebHandler.google_search(action))  # reuse logic

            elif action_type == "google_search":
                from app.commands.handlers.web_handler import WebHandler
                responses.append(WebHandler.google_search(action))

            elif action_type == "open_chatgpt":
                from app.commands.handlers.web_handler import WebHandler
                responses.append(WebHandler.open_chatgpt(action))

        return " | ".join(responses) if responses else "Unknown command"