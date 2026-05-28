import os


class SystemController:
    @staticmethod
    def shutdown():
        os.system("shutdown /s /t 1")

    @staticmethod
    def restart():
        os.system("shutdown /r /t 1")