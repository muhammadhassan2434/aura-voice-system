class CommandValidator:

    @staticmethod
    def validate(data: dict):

        actions = data.get("actions", [])

        # -------------------------
        # MUST HAVE ACTIONS
        # -------------------------
        if not actions:
            return False, "No actions detected"

        # -------------------------
        # VALIDATE EACH ACTION
        # -------------------------
        for action in actions:

            action_type = action.get("type")

            if not action_type:
                return False, "Invalid action type"

            if action_type == "google_search" and not action.get("query"):
                return False, "Missing search query"

            if action_type == "search_chatgpt" and not action.get("query"):
                return False, "Missing ChatGPT query"

            if action_type == "open_project" and not action.get("project_name"):
                return False, "Missing project name"

        return True, "Valid command"