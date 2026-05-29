import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

    def listen(self, show_status=True):

        with sr.Microphone() as source:

            if show_status:
                print("Listening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            print(f"You said: {text}")

            return text.lower()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            return ""