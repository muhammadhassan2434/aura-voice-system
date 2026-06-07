from app.nlp.normalizer import TextNormalizer


class CommandParser:

    @staticmethod
    def parse(command: str):

        normalized = TextNormalizer.normalize(command)

        actions = []

        # ----------------------------
        # CLEAN TEXT
        # ----------------------------
        text = normalized

        remove_words = [
            "and", "then", "please", "karo", "aur", "on", "in", "for"
        ]

        for w in remove_words:
            text = text.replace(w, "")

        text = text.strip()

        # ----------------------------
        # YOUTUBE
        # ----------------------------
        if "youtube" in text:

            actions.append({
                "type": "open_website",
                "name": "youtube"
            })

        # ----------------------------
        # CHATGPT
        # ----------------------------
        if "chatgpt" in text or "gpt" in text:

            actions.append({
                "type": "open_website",
                "name": "chatgpt"
            })

        # ----------------------------
        # GOOGLE SEARCH (smart extract)
        # ----------------------------
        if "search" in text:

            query = text.replace("youtube", "")
            query = query.replace("chatgpt", "")
            query = query.replace("google", "")
            query = query.replace("search", "")
            query = query.strip()

            if query:
                actions.append({
                    "type": "google_search",
                    "query": query
                })

        # ----------------------------
        # FALLBACK
        # ----------------------------
        if not actions:
            actions.append({
                "type": "unknown",
                "query": text
            })

        return {
            "actions": actions
        }