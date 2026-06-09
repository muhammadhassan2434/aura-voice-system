from app.commands.registry import COMMAND_REGISTRY


class CommandDispatcher:

    @staticmethod
    def dispatch(data):

        actions = data.get("actions", [])

        responses = []

        for action in actions:

            action_type = action.get("type")

            # -------------------------
            # SAFETY: invalid action guard
            # -------------------------
            if not action_type:
                responses.append("Invalid action")
                continue

            handler = COMMAND_REGISTRY.get(action_type)

            if not handler:
                responses.append(f"Unknown action: {action_type}")
                continue

            try:
                result = handler(action)

                if result:
                    responses.append(result)
                else:
                    responses.append(f"Executed {action_type}")

            except Exception:
                responses.append(f"Error executing {action_type}")

        return " | ".join(responses) if responses else "No action found"