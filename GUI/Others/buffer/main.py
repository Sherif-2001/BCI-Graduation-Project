# main.py
from PyQt5 import QtWidgets, QtCore
from login import LoginPageMainWindow
from patients import PatientsMainWindow
from calibration_screen import MainWindowApp as CalibrationMainWindow
from session import Ui_MainWindow as SessionMainWindow

from record_automation import Ui_MainWindow as AutomationMainWindow

from newpatient import NewPatientMainWindow


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

        self.new_patient_window = NewPatientMainWindow()

        self.automation_window = AutomationMainWindow()


        # Connect custom signals
        self.login_window.login_successful.connect(self.show_patients_window)
        self.patients_window.go_back.connect(self.show_login_window)
        self.patients_window.go_to_calibration.connect(self.show_calibration_window)
        self.patients_window.go_to_session.connect(self.show_session_window)
        # self.session_ui.menuBack.triggered.connect(self.show_patients_window)
        self.patients_window.go_to_new_patient.connect(self.show_new_patient_window)

        self.patients_window.go_back.connect(self.show_login_window)
        self.calibration_window.go_back.connect(self.show_patients_window)

        self.session_ui.go_back.connect(self.show_patients_window)
        self.session_ui.go_to_automation.connect(self.show_automation_window)


    def show_automation_window(self):
        # self.session_window.hide()
        self.automation_window.show()



    def show_login_window(self):
        self.calibration_window.hide()
        self.session_window.hide()
        self.patients_window.hide()
        self.login_window.show()

    def show_patients_window(self):
        self.login_window.hide()
        self.calibration_window.hide()
        self.session_window.hide()
        self.new_patient_window.hide()
        self.patients_window.show()

    def show_calibration_window(self):
        self.patients_window.hide()
        self.calibration_window.show()

    def show_session_window(self):
        self.patients_window.hide()
        self.session_window.show()

    def show_new_patient_window(self):
        self.patients_window.hide()
        self.new_patient_window.show()

    def run(self):
        self.login_window.show()
        self.app.exec_()

if __name__ == "__main__":
    controller = MainController()
    controller.run()
