import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 7")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)
        animationText = QLabel("Animation")
        self.NumberOfObjects = QLineEdit()

        layout.addWidget(animationText)
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
        self.resultatObjects = int(self.NumberOfObjects.text())


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()