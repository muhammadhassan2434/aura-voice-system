import logging
import os
from datetime import datetime

class Logger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            filename="logs/app.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

        self.logger = logging.getLogger()

    def info(self, message: str):
        self.logger.info(message)
        print(f"[INFO] {message}")

    def error(self, message: str):
        self.logger.error(message)
        print(f"[ERROR] {message}")

    def warning(self, message: str):
        self.logger.warning(message)
        print(f"[WARNING] {message}")