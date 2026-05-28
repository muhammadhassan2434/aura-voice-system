import subprocess


class AppOpener:
    @staticmethod
    def open_chrome():
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    @staticmethod
    def open_vscode():
        subprocess.Popen("code")