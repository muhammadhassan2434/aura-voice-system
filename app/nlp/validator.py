class CommandValidator:

    @staticmethod
    def validate(data: dict):

        intent = data.get("intent")

        if not intent:
            return False, "No intent detected"

        # Google search validation
        if intent == "google_search":
            if not data.get("query"):
                return False, "Missing search query"

        # ChatGPT validation
        if intent == "search_chatgpt":
            if not data.get("query"):
                return False, "Missing ChatGPT query"

        # Open project validation
        if intent == "open_project":
            if not data.get("project_name"):
                return False, "Missing project name"

        return True, "Valid command"