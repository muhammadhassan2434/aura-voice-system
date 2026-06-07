import speech_recognition as sr
import time


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.pause_threshold = 0.8
        self.recognizer.non_speaking_duration = 0.4
        self.recognizer.dynamic_energy_threshold = True

        with sr.Microphone() as source:
            print("[INFO] Calibrating microphone...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("[INFO] Microphone ready")

    def listen(self, show_status=True):

        with sr.Microphone() as source:

            try:
                if show_status:
                    print("Listening...")

                audio = self.recognizer.listen(
                    source,
                    timeout=None,        # 🔥 IMPORTANT FIX
                    phrase_time_limit=8  # allow full sentence
                )

            except Exception:
                return None

        try:
            text = self.recognizer.recognize_google(
                audio,
                language="en-US"
            )

            text = text.lower().strip()

            if text:
                print(f"You said: {text}")
                return text

            return None

        except sr.UnknownValueError:
            return None

        except sr.RequestError as e:
            print(f"[ERROR] Speech API failed: {e}")
            time.sleep(1)
            return None