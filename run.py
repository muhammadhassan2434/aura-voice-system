from app.speech.listener import Listener
from app.speech.speaker import Speaker

from app.commands.parser import CommandParser
from app.commands.dispatcher import CommandDispatcher

from app.nlp.validator import CommandValidator
from app.core.logger import Logger

from app.core.memory import Memory


logger = Logger()

listener = Listener()
speaker = Speaker()
memory = Memory()

speaker.speak("Voice assistant started")

try:
    while True:

        command = listener.listen()

        if not command:
            continue

        logger.info(f"User said: {command}")

        parsed_data = CommandParser.parse(command)

        memory.add_command(
            command=command,
            intent=parsed_data["intent"]
        )

        valid, message = CommandValidator.validate(parsed_data)

        if not valid:
            logger.warning(message)
            speaker.speak(message)
            continue

        try:
            response = CommandDispatcher.dispatch(parsed_data)

            logger.info(f"Response: {response}")

            speaker.speak(response)

            if parsed_data["intent"] == "exit":
                break

        except Exception as e:
            logger.error(str(e))
            speaker.speak("Something went wrong")

except KeyboardInterrupt:
    print("\n[INFO] Assistant stopped safely")
    speaker.speak("Goodbye boss")