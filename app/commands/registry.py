from app.commands.handlers.app_handler import AppHandler
from app.commands.handlers.web_handler import WebHandler

COMMAND_REGISTRY = {

    # APPS
    "open_app": AppHandler.open_app,

    # WEB
    "open_youtube": WebHandler.open_youtube,
    "youtube_search": WebHandler.youtube_search,

    "open_chatgpt": WebHandler.open_chatgpt,
    "search_chatgpt": WebHandler.search_chatgpt,

    "open_website": WebHandler.open_website,
    "google_search": WebHandler.google_search,
}