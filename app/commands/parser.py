from app.ai.brain import AIBrain


class CommandParser:

    @staticmethod
    def parse(command: str):

        result = AIBrain.parse(command)

        return {
            "intent": "ai_mode",
            "actions": result.get("actions", [])
        }