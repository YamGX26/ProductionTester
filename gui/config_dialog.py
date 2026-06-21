from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout
)


class ConfigDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Configuration")

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel("Phase 1 Configuration Window")
        )

        self.setLayout(layout)