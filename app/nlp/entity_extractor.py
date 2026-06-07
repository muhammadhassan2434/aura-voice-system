IGNORE_WORDS = ["karo", "open", "please", "aur", "and", "the", "please"]

class EntityExtractor:

    @staticmethod
    def extract(command: str, intent: str):

        words = command.split()

        clean_words = [w for w in words if w not in IGNORE_WORDS]

        entities = {}

        if intent == "open_website":

            for w in clean_words:
                if w in ["youtube", "chatgpt", "google"]:
                    entities["name"] = w
                    entities["type"] = "website"

        if intent == "open_app":

            for w in clean_words:
                if w in ["chrome", "notepad", "vscode"]:
                    entities["name"] = w
                    entities["type"] = "app"

        return entities