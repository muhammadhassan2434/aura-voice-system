from app.speech.listener import Listener
from app.speech.speaker import Speaker

from app.commands.parser import CommandParser
from app.commands.dispatcher import CommandDispatcher

from app.nlp.validator import CommandValidator
from app.core.logger import Logger
from app.core.memory import Memory
from app.core.wake_detector import WakeDetector
from app.core.safety import Safety


logger = Logger()

listener = Listener()
speaker = Speaker()
memory = Memory()

speaker.speak("Aura assistant started")

ACTIVE_MODE = False

try:

    while True:

        command = listener.listen(show_status=ACTIVE_MODE)

        if not command:
            continue

        logger.info(f"User said: {command}")

        # ----------------------------------------
        # WAKE WORD DETECTION
        # ----------------------------------------
        if not ACTIVE_MODE:

         if WakeDetector.detect(command):
            ACTIVE_MODE = True
            speaker.speak("Yes boss, I am listening")

         continue   # MUST stop here

        # ----------------------------------------
        # PARSE COMMAND
        # ----------------------------------------
        parsed_data = CommandParser.parse(command, memory)

        memory.update(command, parsed_data)

        valid, message = CommandValidator.validate(parsed_data)

        if not valid:
            logger.warning(message)
            speaker.speak(message)
            ACTIVE_MODE = False
            continue

        try:

            actions = parsed_data.get("actions", [])

            # -------------------------
            # SAFETY CHECK
            # -------------------------
            risk = Safety.check(actions)

            if risk == "dangerous":

                speaker.speak("This is a dangerous action. Are you sure boss?")

                confirm = listener.listen()

                if "yes" not in confirm.lower():
                 speaker.speak("Cancelled")
                 ACTIVE_MODE = False
                 continue

                speaker.speak("Okay executing boss")

            elif risk == "medium":

                speaker.speak("Confirm action boss?")

                confirm = listener.listen()

                if "yes" not in confirm.lower():
                    speaker.speak("Cancelled")
                    ACTIVE_MODE = False
                    continue

            # -------------------------
            # EXECUTE COMMAND (MISSING LINE FIXED)
            # -------------------------
            response = CommandDispatcher.dispatch(parsed_data)

            logger.info(f"Response: {response}")

            # -------------------------
            # EXIT CHECK
            # -------------------------
            is_exit = any(a.get("type") == "exit" for a in actions)

            if is_exit:
                speaker.speak(response or "Goodbye boss")
                break

            # -------------------------
            # SPEAK RESPONSE
            # -------------------------
            if response:
                speaker.speak(response)

            # BACK TO SLEEP
            ACTIVE_MODE = False


        except Exception as e:

            logger.error(str(e))
            speaker.speak("Something went wrong")

            ACTIVE_MODE = False


except KeyboardInterrupt:

    print("\n[INFO] Assistant stopped safely")

    speaker.speak("Goodbye boss")

finally:

    speaker.close()
