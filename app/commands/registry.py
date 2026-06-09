from app.commands.handlers.app_handler import AppHandler
from app.commands.handlers.web_handler import WebHandler
from app.commands.handlers.system_handler import SystemHandler


COMMAND_REGISTRY = {

    # APPS
    "open_app": AppHandler.open_app,

    # WEB (UNIFIED)
    "open_website": WebHandler.open_website,
    "search_website": WebHandler.google_search,

    # PLATFORM SPECIFIC (optional fallback)
    "open_youtube": WebHandler.open_youtube,
    "search_youtube": WebHandler.youtube_search,

    "open_chatgpt": WebHandler.open_chatgpt,
    "search_chatgpt": WebHandler.search_chatgpt,

    "google_search": WebHandler.google_search,

    # SYSTEM
    "restart": SystemHandler.restart,
    "shutdown": SystemHandler.shutdown,
}