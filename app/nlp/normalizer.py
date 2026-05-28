import re


class TextNormalizer:

    @staticmethod
    def normalize(text: str):

        text = text.lower()

        # ❌ DO NOT remove dots (VERY IMPORTANT for files)
        text = re.sub(r"[^a-zA-Z0-9.\s]", "", text)

        text = " ".join(text.split())

        return text