from app.commands.registry import COMMAND_REGISTRY


class CommandDispatcher:

    @staticmethod
    def dispatch(data):

        actions = data.get("actions", [])

        responses = []

        for action in actions:

            action_type = action.get("type")

            handler = COMMAND_REGISTRY.get(action_type)

            if handler:

                response = handler(action)

                if response:
                    responses.append(response)

            else:
                responses.append(f"Unknown action: {action_type}")

        return " | ".join(responses) if responses else "Unknown command"