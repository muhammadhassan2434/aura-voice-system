import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.7
        self.recognizer.non_speaking_duration = 0.3
        self.recognizer.dynamic_energy_threshold = True

        with sr.Microphone() as source:
            print("[INFO] Calibrating microphone noise...")
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )
            print("[INFO] Microphone ready")

    def listen(self, show_status=True):

        with sr.Microphone() as source:

            if show_status:
                print("Listening...")

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=6
                )
            except sr.WaitTimeoutError:
                return ""

        try:

            text = self.recognizer.recognize_google(
                audio,
                language="en-US"
            )

            print(f"You said: {text}")

            return text.lower()

        except sr.UnknownValueError:
            print("[INFO] Could not understand audio")
            return ""

        except sr.RequestError as error:
            print(f"[ERROR] Speech recognition service failed: {error}")
            return ""
