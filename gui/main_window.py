from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout
)

from PySide6.QtCore import QTimer
from datetime import datetime

from gui.details_dialog import DetailsDialog
from gui.settings_dialog import SettingsDialog
from gui.config_dialog import ConfigDialog

class MainWindow(QMainWindow):

    def __init__(self, config):

        super().__init__()

        self.config = config

        self.setWindowTitle(
            config["app_name"]
        )

        self.resize(1200, 800)

        self.operator_id = ""
        self.shift = ""
        self.model = ""

        self.build_ui()
        self.start_clock()

def start_clock(self):

    self.timer = QTimer()

    self.timer.timeout.connect(
        self.update_datetime
    )

    self.timer.start(1000)

    self.update_datetime()


def update_datetime(self):

    now = datetime.now()

    self.date_label.setText(
        f"Date: {now:%Y-%m-%d}"
    )

    self.time_label.setText(
        f"Time: {now:%I:%M:%S %p}"
    )

def log(self, message):

    timestamp = datetime.now().strftime(
        "%H:%M:%S"
    )

    self.console.append(
        f"{timestamp} INFO {message}"
    )

def start_test(self):

    serial = self.serial_edit.text().strip()

    if not all([
        self.operator_id,
        self.shift,
        self.model,
        serial
    ]):
        QMessageBox.warning(
            self,
            "Missing Data",
            "Complete all details."
        )
        return

    self.result_label.setText("PASS")

    self.log("Test Started")
    self.log("PASS")

    self.serial_edit.clear()
    self.serial_edit.setFocus()

def open_details(self):

    dlg = DetailsDialog(self)

    if dlg.exec():

        self.operator_id = dlg.id_edit.text()
        self.shift = dlg.shift_edit.text()
        self.model = dlg.model_edit.text()

        self.id_value.setText(
            self.operator_id
        )

        self.shift_value.setText(
            self.shift
        )

        self.model_value.setText(
            self.model
        )

        self.log("Details Updated")

def open_settings(self):

    dlg = SettingsDialog(
        self.config["test_mode"]
    )

    if dlg.exec():

        mode = dlg.selected_mode()

        self.config["test_mode"] = mode

        self.mode_label.setText(
            f"Test Mode: {mode}"
        )

        self.log(
            f"Mode Changed: {mode}"
        )

