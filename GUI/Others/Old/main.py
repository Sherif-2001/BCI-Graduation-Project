# main.py
from PyQt5 import QtWidgets, QtCore
from login import LoginPageMainWindow
from patients import PatientsMainWindow
from calibration_screen import MainWindowApp as CalibrationMainWindow
from session import Ui_MainWindow as SessionMainWindow

class MainController(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.app = QtWidgets.QApplication([])
        self.login_window = LoginPageMainWindow()
        self.patients_window = PatientsMainWindow()
        self.calibration_window = CalibrationMainWindow()
        self.session_window = QtWidgets.QMainWindow()
        self.session_ui = SessionMainWindow()
        self.session_ui.setupUi(self.session_window)

        # Connect custom signals
        self.login_window.login_successful.connect(self.show_patients_window)
        self.patients_window.go_back.connect(self.show_login_window)
        self.patients_window.go_to_calibration.connect(self.show_calibration_window)
        self.patients_window.go_to_session.connect(self.show_session_window)
        # self.calibration_window.ui.menuBack.triggered.connect(self.show_patients_window)
        # self.session_ui.menuBack.triggered.connect(self.show_patients_window)

    def show_login_window(self):
        self.calibration_window.hide()
        self.session_window.hide()
        self.patients_window.hide()
        self.login_window.show()

    def show_patients_window(self):
        self.login_window.hide()
        self.calibration_window.hide()
        self.session_window.hide()
        self.patients_window.show()

    def show_calibration_window(self):
        self.patients_window.hide()
        self.calibration_window.show()

    def show_session_window(self):
        self.patients_window.hide()
        self.session_window.show()

    def run(self):
        self.login_window.show()
        self.app.exec_()

if __name__ == "__main__":
    controller = MainController()
    controller.run()
