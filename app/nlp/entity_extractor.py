class EntityExtractor:

    @staticmethod
    def extract(command: str, intent: str):

        command = command.lower()

        data = {}

        # GOOGLE SEARCH
        if intent == "google_search":

            for phrase in ["google", "search for", "search"]:

                command = command.replace(phrase, "")

            data["query"] = command.strip()

        # CHATGPT SEARCH
        elif intent == "open_chatgpt":

            for phrase in ["open", "chatgpt", "gpt"]:

                command = command.replace(phrase, "")

            data["query"] = command.strip()

        # PROJECT OPEN
        elif intent == "open_project":

            words = command.split()

            if "project" in words:
                idx = words.index("project")

                if idx + 1 < len(words):
                    data["project_name"] = words[idx + 1]

        return data