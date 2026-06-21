import sys

from PySide6.QtWidgets import QApplication

from services.config_manager import (
    ConfigManager
)

from gui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    config = ConfigManager.load()

    window = MainWindow(config)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()