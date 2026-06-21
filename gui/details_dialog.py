from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout
)


class DetailsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Operator Details")

        self.id_edit = QLineEdit()
        self.shift_edit = QLineEdit()
        self.model_edit = QLineEdit()

        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")

        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        layout = QGridLayout()

        layout.addWidget(QLabel("ID"), 0, 0)
        layout.addWidget(self.id_edit, 0, 1)

        layout.addWidget(QLabel("Shift"), 1, 0)
        layout.addWidget(self.shift_edit, 1, 1)

        layout.addWidget(QLabel("Model"), 2, 0)
        layout.addWidget(self.model_edit, 2, 1)

        layout.addWidget(ok_btn, 3, 0)
        layout.addWidget(cancel_btn, 3, 1)

        self.setLayout(layout)