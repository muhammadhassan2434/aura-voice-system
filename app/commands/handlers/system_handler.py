import random


class SystemHandler:

    @staticmethod
    def shutdown(data):

        messages = [
            "Bohat tez ho rahe ho, shutdown kar ke mujhe bhi band kar do",
            "Theek hai boss, system band kar raha hoon",
            "Shutdown mode on, phir milte hain",
        ]

        return random.choice(messages)

    @staticmethod
    def restart(data):

        return "Restarting computer"

    @staticmethod
    def exit_assistant(data):

        return "Goodbye boss"
