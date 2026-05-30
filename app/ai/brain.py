class AIBrain:

    @staticmethod
    def clean_query(text, remove_words):

        for word in remove_words:
            text = text.replace(word, "")

        return text.strip()

    @staticmethod
    def parse(command: str):

        command = command.lower()

        actions = []

        step = 1

        # ------------------------------------------------
        # YOUTUBE
        # ------------------------------------------------
        if "youtube" in command:

            # SEARCH INSIDE YOUTUBE
            if "search" in command or "watch" in command:

                query = AIBrain.clean_query(
                    command,
                    [
                        "open",
                        "youtube",
                        "search",
                        "watch",
                        "for",
                        "about",
                        "on",
                        "and"
                    ]
                )

                actions.append({
                    "step": step,
                    "type": "youtube_search",
                    "query": query
                })

                step += 1

            else:

                actions.append({
                    "step": step,
                    "type": "open_youtube"
                })

                step += 1

        # ------------------------------------------------
        # GOOGLE SEARCH
        # ------------------------------------------------
        elif "google" in command or "search" in command:

            query = AIBrain.clean_query(
                command,
                [
                    "search",
                    "google",
                    "for",
                    "about",
                    "on",
                    "and"
                ]
            )

            actions.append({
                "step": step,
                "type": "google_search",
                "query": query
            })

            step += 1

        # ------------------------------------------------
        # CHATGPT
        # ------------------------------------------------
        if "chatgpt" in command or "gpt" in command:

            if "search" in command:

                query = AIBrain.clean_query(
                    command,
                    [
                        "search",
                        "chatgpt",
                        "gpt",
                        "for",
                        "about",
                        "on",
                        "and"
                    ]
                )

                actions.append({
                    "step": step,
                    "type": "search_chatgpt",
                    "query": query
                })

            else:

                actions.append({
                    "step": step,
                    "type": "open_chatgpt"
                })

            step += 1

        # ------------------------------------------------
        # SYSTEM COMMANDS
        # ------------------------------------------------
        if "shutdown" in command or "band karo" in command:

            actions.append({
                "step": step,
                "type": "shutdown"
            })

            step += 1

        # ------------------------------------------------
        # EXIT
        # ------------------------------------------------
        if "exit" in command or "close assistant" in command:

            actions.append({
                "step": step,
                "type": "exit"
            })

            step += 1

        # ------------------------------------------------
        # FALLBACK
        # ------------------------------------------------
        if not actions:

            actions.append({
                "step": step,
                "type": "unknown",
                "query": command
            })

        return {
            "intent": "ai_mode",
            "actions": actions
        }
