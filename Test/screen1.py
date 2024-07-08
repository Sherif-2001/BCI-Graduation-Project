from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
import sys

class Screen1(QWidget):
    
    def __init__(self, switch_function=None):
        self.visit_count = 0
        super().__init__()
        
        self.initUI(switch_function)

    def increment_count (self):
        self.visit_count += 1

    def initUI(self, switch_function):
        self.setWindowTitle("Screen 1")

        layout = QVBoxLayout()

        self.counter_label = QLabel(f'Visit count: {self.visit_count}', self)
        layout.addWidget(self.counter_label)

        self.text_field = QLineEdit(self)
        self.text_field.setPlaceholderText('Enter some text')
        layout.addWidget(self.text_field)

        btn = QPushButton('Go to Screen 2', self)
        if switch_function:
            btn.clicked.connect(switch_function)
        layout.addWidget(btn)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Screen1()
    ex.show()
    sys.exit(app.exec_())
