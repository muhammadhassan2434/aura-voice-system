from app.config.wake_words import WAKE_WORDS


class WakeDetector:

    @staticmethod
    def detect(command: str):

        command = command.lower()

        for wake_word in WAKE_WORDS:

            if wake_word in command:
                return True

        return False