from app.config.wake_words import WAKE_WORDS
import re

class WakeDetector:


    @staticmethod
    def detect(text):

        text = text.lower().strip()

        # normalize spaces
        text = re.sub(r'\s+', ' ', text)

        for word in WAKE_WORDS:

            # exact word match (prevents aurora issue)
            pattern = r'\b' + re.escape(word) + r'\b'

            if re.search(pattern, text):
                return True

        return False