from app.nlp.normalizer import TextNormalizer
from app.nlp.intent_matcher import IntentMatcher


class CommandParser:

    @staticmethod
    def parse(command: str):

        normalized_command = TextNormalizer.normalize(command)

        words = normalized_command.split()   # ✅ ALWAYS DEFINED FIRST

        intent = IntentMatcher.match_intent(normalized_command)

        data = {
            "intent": intent
        }

        # Google search
        if "search google for" in normalized_command:

            query = normalized_command.replace(
                "search google for",
                ""
            ).strip()

            data["intent"] = "google_search"
            data["query"] = query

        # Open project
        if "project" in words:

            index = words.index("project")

            if index + 1 < len(words):

                project_name = words[index + 1]

                data["intent"] = "open_project"
                data["project_name"] = project_name

        # Debug
        print(f"Normalized: {normalized_command}")
        print(f"Detected Intent: {data['intent']}")

        return data