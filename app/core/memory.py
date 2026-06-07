class Memory:

    def __init__(self):
        self.last_command = None
        self.last_actions = []
        self.last_query = None
        self.history = []

    # -----------------------
    # SAVE COMMAND
    # -----------------------
    def update(self, command, parsed_data):

        self.last_command = command
        self.history.append(command)

        actions = parsed_data.get("actions", [])

        self.last_actions = actions

        # extract query if exists
        for action in actions:
            if "query" in action:
                self.last_query = action["query"]

    # -----------------------
    # CONTEXT HELPERS
    # -----------------------
    def get_last_query(self):
        return self.last_query

    def get_last_actions(self):
        return self.last_actions

    def get_last_command(self):
        return self.last_command