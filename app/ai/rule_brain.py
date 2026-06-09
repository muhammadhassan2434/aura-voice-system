class AIBrain:

    @staticmethod
    def parse(command: str):

        command = command.lower().strip()
        actions = []

        # -------------------------
        # YOUTUBE
        # -------------------------
        if "youtube" in command:

            if "search" in command:

                query = command
                for w in ["open", "youtube", "search", "and", "on", "for", "about"]:
                    query = query.replace(w, "")

                query = " ".join(query.split())

                actions.append({
                    "type": "search_youtube",
                    "query": query
                })

            else:

                actions.append({
                    "type": "open_youtube"
                })

        # -------------------------
        # GOOGLE
        # -------------------------
        elif "google" in command or "search" in command:

            query = command
            for w in ["google", "search", "open", "for", "about"]:
                query = query.replace(w, "")

            query = " ".join(query.split())

            actions.append({
                "type": "google_search",
                "query": query
            })

        # -------------------------
        # CHATGPT
        # -------------------------
        elif "chatgpt" in command or "gpt" in command:

            if "search" in command:

                query = command.replace("chatgpt", "").replace("gpt", "").replace("search", "")
                query = " ".join(query.split())

                actions.append({
                    "type": "search_chatgpt",
                    "query": query
                })

            else:

                actions.append({
                    "type": "open_chatgpt"
                })

        # -------------------------
        # FALLBACK
        # -------------------------
        else:
            actions.append({
                "type": "google_search",
                "query": command
            })

        return {
            "intent": "multi_action",
            "actions": actions
        }