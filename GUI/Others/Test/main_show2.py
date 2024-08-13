from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import QTimer
import sys

class Screen1(QWidget):
    def __init__(self, switch_function=None):
        super().__init__()
        self.visit_count = 0
        self.initUI(switch_function)
        self.start_timer()

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

    def start_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.increment_counter)
        self.timer.start(1000)  # Increment counter every second

    def increment_counter(self):
        self.visit_count += 1
        self.update_counter()

    def update_counter(self):
        self.counter_label.setText(f'Visit count: {self.visit_count}')

class Screen2(QWidget):
    def __init__(self, switch_function=None):
        super().__init__()
        self.initUI(switch_function)

    def initUI(self, switch_function):
        self.setWindowTitle("Screen 2")

        layout = QVBoxLayout()

        btn = QPushButton('Go to Screen 1', self)
        if switch_function:
            btn.clicked.connect(switch_function)
        layout.addWidget(btn)

        self.setLayout(layout)

class MainController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.screen1 = Screen1(self.show_screen2)
        self.screen2 = Screen2(self.show_screen1)
        self.current_screen = self.screen1

    def show_screen1(self):
        self.screen1.show()

    def show_screen2(self):
        self.screen2.show()

    def run(self):
        self.screen1.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    controller = MainController()
    controller.run()

