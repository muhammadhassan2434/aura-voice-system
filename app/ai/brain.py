from app.ai.gpt_brain import GPTBrain
from app.ai.rule_brain import AIBrain  # your old brain


class Brain:

    USE_AI = False  # 🔥 later we turn this True

    @staticmethod
    def parse(command: str):

        # -------------------------
        # AI MODE (future GPT)
        # -------------------------
        if Brain.USE_AI:
            return GPTBrain.parse(command)

        # -------------------------
        # RULE MODE (current fallback)
        # -------------------------
        return AIBrain.parse(command)