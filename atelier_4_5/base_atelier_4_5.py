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
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)
        nbOfObjectsText = QLabel("Number of objects")
        self.NumberOfObjects = QLineEdit()
        self.minX =  QLineEdit("minX")
        self.minY =  QLineEdit("minY")
        self.minZ =  QLineEdit("minZ")
        self.maxX =  QLineEdit("maxX")
        self.maxY =  QLineEdit("maxY")
        self.maxZ =  QLineEdit("maxZ")
        self.minScale = QLineEdit("minScale")
        self.maxScale = QLineEdit("maxScale")

        layout.addWidget(nbOfObjectsText)
        layout.addWidget(self.NumberOfObjects)
        layout.addWidget(self.minX)
        layout.addWidget(self.minY)
        layout.addWidget(self.minZ)
        layout.addWidget(self.maxX)
        layout.addWidget(self.maxY)
        layout.addWidget(self.maxZ)
        layout.addWidget(self.minScale)
        layout.addWidget(self.maxScale)
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
        self.resultatObjects = int(self.NumberOfObjects.text())
        for i in range(self.resultatObjects):

            forme = random.choice(["cube", "cylindre", "sphere"])

            if forme == "cube":
                objet = cmds.polyCube()[0]
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            random_x = random.uniform(float(self.minX.text()),float(self.maxX.text()))
            random_y = random.uniform(float(self.minY.text()),float(self.maxY.text()))
            random_z = random.uniform(float(self.minZ.text()),float(self.maxZ.text()))
            random_s = random.uniform(float(self.minScale.text()),float(self.maxScale.text()))
            cmds.move(random_x, random_y, random_z, objet)
            cmds.scale(random_s,random_s,random_s)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()