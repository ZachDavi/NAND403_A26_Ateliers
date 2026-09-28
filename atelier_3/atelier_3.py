from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
 
class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        text_edit = QTextEdit()
        button = QPushButton("CLIQUE MOI")
        button.clicked.connect(self.on_click())
        layout.addWidget(label)
        layout.addWidget(text_edit)
        layout.addWidget(button)

    def on_click(self):
        print("caca")
        message_button = QMessageBox()
        layout = QVBoxLayout(self)
        layout.addWidget(message_button)
        message_button.setText("Caca")
    
def main():
    global widget
    widget.close()
    widget = MessageBoard()
    widget.show()
 
main()