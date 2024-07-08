from PyQt5.QtWidgets import QApplication
import sys
from screen1 import Screen1
from screen2 import Screen2

class MainController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.screen1 = Screen1(self.show_screen2)
        self.screen2 = Screen2(self.show_screen1)
        self.current_screen = self.screen1

    def show_screen1(self):
        self.screen2.close()
        self.screen1.show()
        self.current_screen = self.screen1

    def show_screen2(self):
        self.screen1.close()
        self.screen2.show()
        self.current_screen = self.screen2

    def run(self):
        self.current_screen.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    controller = MainController()
    controller.run()
