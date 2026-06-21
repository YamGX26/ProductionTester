from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout   
)

from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from datetime import datetime

from gui.details_dialog import DetailsDialog
from gui.settings_dialog import SettingsDialog
from gui.config_dialog import ConfigDialog


class MainWindow(QMainWindow):

    def __init__(self, config):

        super().__init__()

        self.config = config

        self.setWindowTitle(config["app_name"])
        self.resize(1200, 800)

        self.operator_id = ""
        self.shift = ""
        self.model = ""

        self.build_ui()
        self.start_clock()
        self.apply_theme()

    # ---------------- UI ----------------
    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        grid = QGridLayout()

    # ================= HEADER =================
        self.date_label = QLabel("Date:")
        self.time_label = QLabel("Time:")
        self.mode_label = QLabel(f"Test Mode: {self.config['test_mode']}")

        header = QHBoxLayout()
        header.addWidget(QLabel("LOGO"))
        header.addWidget(QLabel(self.config["app_name"]))
        header.addStretch()
        header.addWidget(self.date_label)
        header.addWidget(self.time_label)
        header.addWidget(self.mode_label)

        grid.addLayout(header, 0, 0, 1, 2)

    # ================= OPERATOR =================
        self.id_value = QLabel("")
        self.shift_value = QLabel("")
        self.model_value = QLabel("")
        self.serial_edit = QLineEdit()

        op_layout = QVBoxLayout()
        op_layout.addWidget(QLabel("ID"))
        op_layout.addWidget(self.id_value)
        op_layout.addWidget(QLabel("Shift"))
        op_layout.addWidget(self.shift_value)
        op_layout.addWidget(QLabel("Model"))
        op_layout.addWidget(self.model_value)
        op_layout.addWidget(QLabel("Serial"))
        op_layout.addWidget(self.serial_edit)

        grid.addLayout(op_layout, 1, 0)

    # ================= CONTROL PANEL =================
        control_layout = QVBoxLayout()

        start_btn = QPushButton("Start")
        details_btn = QPushButton("Details")
        settings_btn = QPushButton("Settings")
        config_btn = QPushButton("Config")
        exit_btn = QPushButton("Exit")

        start_btn.clicked.connect(self.start_test)
        details_btn.clicked.connect(self.open_details)
        settings_btn.clicked.connect(self.open_settings)
        config_btn.clicked.connect(self.open_config)
        exit_btn.clicked.connect(self.close)

        control_layout.addWidget(start_btn)
        control_layout.addWidget(details_btn)
        control_layout.addWidget(settings_btn)
        control_layout.addWidget(config_btn)
        control_layout.addWidget(exit_btn)

        grid.addLayout(control_layout, 2, 0)

    # ================= TEST RESULT AREA =================
        self.result_label = QLabel("")
        self.result_label.setStyleSheet("font-size: 48px; font-weight: bold;")
        self.result_label.setAlignment(Qt.AlignCenter)

        grid.addWidget(self.result_label, 1, 1)

    # ================= CONSOLE =================
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setStyleSheet("""
            background-color: #0f0f0f;
            color: #00ff88;
            font-family: Consolas;
            font-size: 11px;
        """)

        grid.addWidget(self.console, 2, 1)

        central.setLayout(grid)

    # ---------------- CLOCK ----------------
    def start_clock(self):

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)
        self.update_datetime()

    def update_datetime(self):

        now = datetime.now()

        self.date_label.setText(f"Date: {now:%Y-%m-%d}")
        self.time_label.setText(f"Time: {now:%I:%M:%S %p}")

    # ---------------- LOG ----------------
    def log(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.append(f"{timestamp} INFO {message}")

    # ---------------- TEST ----------------
    def start_test(self):

        serial = self.serial_edit.text().strip()

        if not all([self.operator_id, self.shift, self.model, serial]):
            QMessageBox.warning(self, "Missing Data", "Complete all details.")
            return

        self.result_label.setText("PASS")
        self.result_label.setStyleSheet(
            "color: #00ff88; font-size: 48px; font-weight: bold;"
        )

        self.log("Test Started")
        self.log("PASS")

        self.serial_edit.clear()
        self.serial_edit.setFocus()

    # ---------------- DETAILS ----------------
    def open_details(self):

        dlg = DetailsDialog(self)

        if dlg.exec():

            self.operator_id = dlg.id_edit.text()
            self.shift = dlg.shift_edit.text()
            self.model = dlg.model_edit.text()

            self.id_value.setText(self.operator_id)
            self.shift_value.setText(self.shift)
            self.model_value.setText(self.model)

            self.log("Details Updated")

    # ---------------- SETTINGS ----------------
    def open_settings(self):

        dlg = SettingsDialog(self.config["test_mode"])

        if dlg.exec():

            mode = dlg.selected_mode()

            self.config["test_mode"] = mode
            self.mode_label.setText(f"Test Mode: {mode}")

            self.log(f"Mode Changed: {mode}")

    # ---------------- CONFIG ----------------
    def open_config(self):

        dlg = ConfigDialog()
        dlg.exec()


    def apply_theme(self):

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }

            QLabel {
                color: #dcdcdc;
                font-size: 12px;
            }

            QPushButton {
                background-color: #2d2d2d;
                color: white;
                padding: 6px;
                border: 1px solid #444;
                border-radius: 4px;
            }

            QPushButton:hover {
                background-color: #3a3a3a;
            }

            QPushButton:pressed {
                background-color: #555;
            }

            QLineEdit {
                background-color: #2b2b2b;
                color: white;
                border: 1px solid #444;
                padding: 4px;
            }

            QTextEdit {
                background-color: #121212;
                color: #00ff88;
                border: 1px solid #333;
            }
        """)    
