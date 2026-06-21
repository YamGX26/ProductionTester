import json
import os

CONFIG_FILE = "config/config.json"


class ConfigManager:

    @staticmethod
    def load():

        if not os.path.exists(CONFIG_FILE):
            return {
                "app_name": "Production Tester",
                "test_mode": "Development",
                "logo_path": "assets/logo.png",
                "com_port": "COM1",
                "log_path": "./logs"
            }

        with open(CONFIG_FILE, "r") as file:
            return json.load(file)

    @staticmethod
    def save(data):

        os.makedirs("config", exist_ok=True)

        with open(CONFIG_FILE, "w") as file:
            json.dump(data, file, indent=4)