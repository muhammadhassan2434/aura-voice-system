class Memory:

    def __init__(self):
        self.history = []
        self.last_command = None
        self.last_intent = None

        # simple user preferences (expand later)
        self.preferences = {}

    def add_command(self, command: str, intent: str):
        self.history.append({
            "command": command,
            "intent": intent
        })

        self.last_command = command
        self.last_intent = intent

    def get_history(self):
        return self.history[-10:]  # last 10 commands

    def set_preference(self, key, value):
        self.preferences[key] = value

    def get_preference(self, key):
        return self.preferences.get(key, None)