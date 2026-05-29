from app.config.commands import COMMAND_KEYWORDS


class IntentMatcher:

    @staticmethod
    def match_intent(command: str):

        command = command.lower()

        matched_intents = []

        for intent, keywords in COMMAND_KEYWORDS.items():

            for word in keywords:

                if word in command:
                    matched_intents.append(intent)
                    break

        if not matched_intents:
            return "unknown"

        return matched_intents[0]