from PySide6.QtWidgets import (
    QDialog,
    QPushButton,
    QVBoxLayout,
    QRadioButton
)


class SettingsDialog(QDialog):

    def __init__(self, current_mode):
        super().__init__()

        self.setWindowTitle("Settings")

        self.prod_radio = QRadioButton("Production")
        self.dev_radio = QRadioButton("Development")

        if current_mode == "Production":
            self.prod_radio.setChecked(True)
        else:
            self.dev_radio.setChecked(True)

        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")

        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        layout = QVBoxLayout()

        layout.addWidget(self.prod_radio)
        layout.addWidget(self.dev_radio)

        layout.addWidget(save_btn)
        layout.addWidget(cancel_btn)

        self.setLayout(layout)

    def selected_mode(self):

        return (
            "Production"
            if self.prod_radio.isChecked()
            else "Development"
        )