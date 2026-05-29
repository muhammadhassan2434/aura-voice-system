from app.automations.web import WebController


class WebHandler:

    @staticmethod
    def open_youtube(data):

        WebController.open_youtube()

        return "Opening YouTube"
    @staticmethod
    def youtube_search(data):

     query = data.get("query", "")

     WebController.search_youtube(query)

     return f"Searching YouTube for {query}"

    @staticmethod
    def google_search(data):

        query = data.get("query")

        WebController.search_google(query)

        return f"Searching Google for {query}"

    @staticmethod
    def open_chatgpt(data):

        WebController.open_chatgpt()

        return "Opening ChatGPT"

    @staticmethod
    def search_chatgpt(data):

        query = data.get("query", "")

        if not query:
            return "Please provide search query"

        WebController.search_chatgpt(query)

        return f"Searching ChatGPT for {query}"