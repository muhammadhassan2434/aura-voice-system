from app.ai.brain import Brain


class CommandParser:

    @staticmethod
    def parse(command: str, memory):

        # 1. get base AI/rule result
        result = Brain.parse(command)

        actions = result.get("actions", [])

        # 2. attach follow-up actions
        follow_actions = CommandParser.resolve_followup(command, memory)

        if follow_actions:
            actions.extend(follow_actions)

        result["actions"] = actions

        print(f"[BRAIN OUTPUT]: {result}")

        return result

    # -------------------------
    # FOLLOW-UP HANDLER
    # -------------------------
    @staticmethod
    def resolve_followup(command, memory):

        command = command.lower()
        actions = []

        last_query = memory.get_last_query()

        if not last_query:
            return actions

        # FIRST RESULT
        if "first result" in command or "open first" in command:
            actions.append({
                "type": "google_search",
                "query": last_query
            })

        # REPEAT
        elif "same" in command or "repeat" in command:
            actions.append({
                "type": "google_search",
                "query": last_query
            })

        return actions