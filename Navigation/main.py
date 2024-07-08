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
        self.patients_window.open_calibration.connect(self.show_calibration_window)
        self.patients_window.open_session.connect(self.show_session_window)
        self.patients_window.open_new_patient.connect(self.show_new_patient_window)
        self.new_patient_window.go_back.connect(self.show_patients_window)

    def show_login_window(self):
        self.login_window.show()
        self.patients_window.close()

    def show_patients_window(self):
        self.patients_window.show()
        self.login_window.close()
        self.calibration_window.close()
        self.session_window.close()
        self.new_patient_window.close()

    def show_calibration_window(self):
        self.calibration_window.show()
        self.patients_window.close()

    def show_session_window(self):
        self.session_window.show()
        self.patients_window.close()

    def show_new_patient_window(self):
        self.new_patient_window.show()
        self.patients_window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = MainController()
    controller.show_login_window()
    sys.exit(app.exec_())
