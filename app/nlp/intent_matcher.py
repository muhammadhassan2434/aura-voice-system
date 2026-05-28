class IntentMatcher:

    COMMANDS = {

        "open_chrome": [
            "open chrome",
            "launch chrome",
            "start chrome",
            "open browser"
        ],

        "open_youtube": [
            "open youtube",
            "launch youtube",
            "start youtube"
        ],

        "shutdown": [
            "shutdown",
            "turn off computer",
            "power off"
        ],

        "restart": [
            "restart",
            "reboot computer"
        ],

        "open_project": [
        "open project",
       "open the project"
        ],

        "open_file": [
            "open file",
            "open"
        ]
    }

    @classmethod
    def match_intent(cls, command: str):

        for intent, patterns in cls.COMMANDS.items():

            for pattern in patterns:

                if pattern in command:
                    return intent

        return "unknown"