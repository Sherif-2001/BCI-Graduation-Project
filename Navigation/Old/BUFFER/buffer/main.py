# main.py

from PyQt5 import QtWidgets
from login import LoginWindow
from patients import PatientsMainWindow
from calibration_screen import CalibrationMainWindow
from session import SessionMainWindow
from newpatient import NewPatientMainWindow

class MainController:
    def __init__(self):
        self.login_window = LoginWindow()
        self.patients_window = PatientsMainWindow()
        self.calibration_window = CalibrationMainWindow()
        self.session_window = SessionMainWindow()
        self.new_patient_window = NewPatientMainWindow()

        self.login_window.login_successful.connect(self.show_patients_window)
        self.patients_window.go_back.connect(self.show_login_window)
        self.patients_window.go_to_calibration.connect(self.show_calibration_window)
        self.patients_window.go_to_session.connect(self.show_session_window)
        self.patients_window.go_to_new_patient.connect(self.show_new_patient_window)
        self.new_patient_window.go_back.connect(self.show_patients_window)

    def show_login_window(self):
        self.patients_window.hide()
        self.calibration_window.hide()
        self.session_window.hide()
        self.new_patient_window.hide()
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = MainController()
    controller.show_login_window()
    sys.exit(app.exec_())
