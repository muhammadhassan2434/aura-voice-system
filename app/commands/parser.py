from app.nlp.normalizer import TextNormalizer
from app.nlp.intent_matcher import IntentMatcher


class CommandParser:

    @staticmethod
    def parse(command: str):

        normalized = TextNormalizer.normalize(command)

        intent = IntentMatcher.match_intent(normalized)

        data = {
            "intent": intent,
            "actions": []
        }

        # STEP SPLITTER (VERY IMPORTANT)
        steps = normalized.replace("then", "|").replace("and", "|").split("|")

        step_index = 0

        for step in steps:

            step = step.strip()

            if not step:
                continue

            step_index += 1

            # -------------------------
            # YOUTUBE ACTION
            # -------------------------
            if "youtube" in step and "search" not in step:
                data["actions"].append({
                    "step": step_index,
                    "type": "open_youtube"
                })

            # -------------------------
            # SEARCH ACTION (SMART)
            # -------------------------
            if "search" in step:

                # DEFAULT
                target = "google"

                # PLATFORM PRIORITY (IMPORTANT FIX)
                if "youtube" in step:
                    target = "youtube"

                elif "chatgpt" in step or "gpt" in step:
                    target = "chatgpt"

                elif "google" in step:
                    target = "google"

                # CLEAN QUERY
                query = step

                for word in ["open", "search", "youtube", "chatgpt", "gpt", "google", "on", "for", "about"]:
                    query = query.replace(word, "")

                query = query.strip()

                if query:

                    data["actions"].append({
                        "step": step_index,
                        "type": f"{target}_search",
                        "query": query
                    })

            # -------------------------
            # CHATGPT OPEN
            # -------------------------
            if "chatgpt" in step and "search" not in step:

                data["actions"].append({
                    "step": step_index,
                    "type": "open_chatgpt"
                })

        # SORT ACTIONS BY STEP (IMPORTANT)
        data["actions"].sort(key=lambda x: x["step"])

        print(f"Normalized: {normalized}")
        print(f"Intent: {intent}")
        print(f"Actions: {data['actions']}")

        return data