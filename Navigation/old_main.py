# main.py
from PyQt5 import QtWidgets, QtCore
from login import LoginPageMainWindow
from patients import PatientsMainWindow

class MainController(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.app = QtWidgets.QApplication([])
        self.login_window = LoginPageMainWindow()
        self.patients_window = PatientsMainWindow()

        # Connect custom signals
        self.login_window.login_successful.connect(self.show_patients_window)
        self.patients_window.go_back.connect(self.show_login_window)

    def show_login_window(self):
        print(" show_login_window ")

        self.patients_window.hide()
        self.login_window.show()

    def show_patients_window(self):
        self.login_window.hide()
        self.patients_window.show()

    def run(self):
        self.login_window.show()
        self.app.exec_()

if __name__ == "__main__":
    controller = MainController()
    controller.run()
