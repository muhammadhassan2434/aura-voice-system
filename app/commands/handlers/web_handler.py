import webbrowser

class WebHandler:

    @staticmethod
    def open_youtube(data):
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    @staticmethod
    def youtube_search(data):
        query = data.get("query", "")
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        return f"Searching YouTube for {query}"

    @staticmethod
    def google_search(data):
        query = data.get("query", "")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching Google for {query}"

    @staticmethod
    def open_chatgpt(data):
        webbrowser.open("https://chatgpt.com")
        return "Opening ChatGPT"

    @staticmethod
    def search_chatgpt(data):
        query = data.get("query", "")
        url = f"https://chatgpt.com/?q={query}"
        webbrowser.open(url)
        return f"Searching ChatGPT for {query}"

    @staticmethod
    def open_website(data):

        name = data.get("name", "").lower().strip()

        WEBSITES = {
            "youtube": "https://youtube.com",
            "chatgpt": "https://chatgpt.com",
            "google": "https://google.com",
            "github": "https://github.com",
        }

        url = WEBSITES.get(name)

        if not url:
            return f"{name} not found"

        webbrowser.open(url)
        return f"Opening {name}"