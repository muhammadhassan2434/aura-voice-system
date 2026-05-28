from app.speech.listener import Listener
from app.speech.speaker import Speaker

from app.commands.parser import CommandParser
from app.commands.executor import CommandExecutor

import time
from app.automations.system import SystemController


listener = Listener()
speaker = Speaker()

speaker.speak("Voice assistant started")

while True:

    command = listener.listen()

    if not command:
        continue

    parsed_data = CommandParser.parse(command)

    response = CommandExecutor.execute(parsed_data)

    message = None
    action = None

    # ✅ SAFE HANDLING
    if isinstance(response, dict):
        message = response.get("message")
        action = response.get("action")

    else:
        message = response

    # 🗣️ SPEAK FIRST
    if message:
        speaker.speak(message)

    # ⚙️ ACTION HANDLER
    if action == "shutdown":
        time.sleep(2)
        SystemController.shutdown()

    # 🚪 EXIT CONDITION
    if parsed_data.get("intent") == "exit":
        break