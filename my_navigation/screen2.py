from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class Screen2(QWidget):
    def __init__(self, switch_function):
        super().__init__()
        self.initUI(switch_function)

    def initUI(self, switch_function):
        self.setWindowTitle("Screen 2")

        layout = QVBoxLayout()

        btn = QPushButton('Go to Screen 1', self)
        btn.clicked.connect(switch_function)

        layout.addWidget(btn)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Screen2()
    ex.show()
    sys.exit(app.exec_())
