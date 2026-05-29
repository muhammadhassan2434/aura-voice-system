from app.commands.handlers.web_handler import WebHandler
from app.commands.handlers.system_handler import SystemHandler
from app.commands.handlers.file_handler import FileHandler
from app.commands.handlers.app_handler import AppHandler

COMMAND_REGISTRY = {

    # APPS
    "open_chrome": AppHandler.open_chrome,

    # WEB
    "open_youtube": WebHandler.open_youtube,
    "google_search": WebHandler.google_search,
    "open_chatgpt": WebHandler.open_chatgpt,
    "search_chatgpt": WebHandler.search_chatgpt,
    "youtube_search": WebHandler.youtube_search,

    # FILES
    "open_project": FileHandler.open_project,

    # SYSTEM
    "shutdown": SystemHandler.shutdown,
    "restart": SystemHandler.restart,
    "exit": SystemHandler.exit_assistant,
}