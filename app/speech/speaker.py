import subprocess

import pyttsx3
from app.config.settings import VOICE_RATE


class Speaker:
    def __init__(self):
        self.engine = None
        self._init_engine()

    def _init_engine(self):
        try:
            self.engine = pyttsx3.init("sapi5")
        except Exception as error:
            self.engine = None
            print(f"[WARNING] pyttsx3 unavailable, using PowerShell speech: {error}")
            return

        self.engine.setProperty("rate", VOICE_RATE)

    def speak(self, text: str):
        if not text:
            return

        print(f"Assistant: {text}")

        if not self.engine:
            self._speak_with_powershell(text)
            return

        for attempt in range(2):
            try:
                self.engine.say(text)
                self.engine.runAndWait()
                return
            except RuntimeError:
                self.engine.stop()
                self._init_engine()
                if not self.engine:
                    self._speak_with_powershell(text)
                    return

        print("[ERROR] Text-to-speech failed")

    def _speak_with_powershell(self, text: str):
        safe_text = text.replace("'", "''")
        rate = max(-10, min(10, int((VOICE_RATE - 170) / 20)))

        command = (
            "Add-Type -AssemblyName System.Speech; "
            "$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
            f"$speaker.Rate = {rate}; "
            f"$speaker.Speak('{safe_text}')"
        )

        try:
            subprocess.run(
                ["powershell.exe", "-NoProfile", "-Command", command],
                check=True
            )
        except Exception as error:
            print(f"[ERROR] PowerShell text-to-speech failed: {error}")

    def close(self):
        if self.engine:
            self.engine.stop()
