class Memory:

    def __init__(self):
        self.last_command = None
        self.last_actions = []
        self.last_query = None
        self.history = []
        self.pending_actions = []  # ✅ FIXED

    def update(self, command, parsed_data):

        self.last_command = command
        self.history.append(command)

        actions = parsed_data.get("actions", [])
        self.last_actions = actions

        for action in actions:
            if "query" in action:
                self.last_query = action["query"]

    def get_last_query(self):
        return self.last_query

    def get_last_actions(self):
        return self.last_actions

    def get_last_command(self):
        return self.last_command

    def set_pending_actions(self, actions):
        self.pending_actions = actions

    def get_pending_actions(self):
        return self.pending_actions