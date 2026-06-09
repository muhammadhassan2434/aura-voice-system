class Safety:

    DANGEROUS_ACTIONS = [
        "shutdown",
        "restart",
        "format",
        "delete_file",
        "system_close"
    ]

    MEDIUM_RISK = [
        "open_app",
        "open_website"
    ]

    @staticmethod
    def check(actions: list):

        for action in actions:

            action_type = action.get("type")

            if action_type in Safety.DANGEROUS_ACTIONS:
                return "dangerous"

            if action_type in Safety.MEDIUM_RISK:
                return "medium"

        return "safe"