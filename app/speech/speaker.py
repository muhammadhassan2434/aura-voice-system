import pyttsx3
from app.config.settings import VOICE_RATE


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

        # IMPORTANT: set voice speed
        self.engine.setProperty("rate", VOICE_RATE)

    def speak(self, text: str):

        print(f"Assistant: {text}")

        self.engine.say(text)
        self.engine.runAndWait()

        # IMPORTANT FIX (sometimes needed on Windows)
        self.engine.stop()