import webbrowser


class WebController:
    @staticmethod
    def open_youtube():
        webbrowser.open("https://youtube.com")

    @staticmethod
    def search_google(query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)