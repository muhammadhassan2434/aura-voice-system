from app.automations.apps import AppOpener


class AppHandler:

    @staticmethod
    def open_chrome(data):

        AppOpener.open_chrome()

        return "Opening Chrome"