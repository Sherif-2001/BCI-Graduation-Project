from PyQt5 import QtWidgets, QtCore
from login import LoginPageMainWindow
from patients import PatientsMainWindow
from calibration_screen import MainWindowApp as CalibrationMainWindow
from session import Ui_MainWindow as SessionMainWindow
from LSLViewer import LSLViewer

from record_automation import Ui_MainWindow as AutomationMainWindow

from report import Ui_MainWindow,Report

from newpatient import NewPatientMainWindow

from functions import *

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, lfilter_zi, firwin
from time import sleep
from pylsl import StreamInlet, resolve_stream
from optparse import OptionParser
import seaborn as sns
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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

        self.ReportPage = QtWidgets.QMainWindow()
        self.report_ui = Ui_MainWindow()
        self.report_ui.setupUi(self.ReportPage )
        # self.report_ui.show()
        # self.ReportPage.show()

        # self.patients_window.ui.patient_name

        self.session_ui.update_patient_name("Sherif Ahmed")


        # Stream for session_window
        # # Setting up the LSLViewer
        # streams = resolve_stream('type', 'EEG')
        # if len(streams) == 0:
        #     raise(RuntimeError("Can't find EEG stream"))
        # lslv = LSLViewer(streams[0], self.session_ui.fig, self.session_ui.axes, window=5, scale=891)
        
        # # Start the LSLViewer
        # lslv.start()


        self.new_patient_window = NewPatientMainWindow()

        self.automation_window = AutomationMainWindow()

        # # Extract EEG stream info
        # self.automation_window.sfreq, self.automation_window.ch_names = AutomationMainWindow.extract_stream_info()
        # self.automation_window.setupUi(self.automation_window)
        # self.automation_window.show()


        # Connect custom signals
        self.login_window.login_successful.connect(self.show_patients_window)
        self.patients_window.go_back.connect(self.show_login_window)
        self.patients_window.go_to_calibration.connect(self.show_calibration_window)
        self.patients_window.go_to_session.connect(self.show_session_window)
        self.patients_window.go_to_new_patient.connect(self.show_new_patient_window)
        self.patients_window.go_back.connect(self.show_login_window)
        self.calibration_window.go_back.connect(self.show_patients_window)

        self.new_patient_window.go_back.connect(self.show_patients_window)
        
        
        # Connect signals for session window
        self.session_ui.go_back.connect(self.show_patients_window)
        # self.session_ui.go_back.connect(self.show_patients_window)
        self.session_ui.go_to_automation.connect(self.start_automation_tasks)

        self.calibration_window.go_to_report.connect(self.show_report_window)

    def show_login_window(self):
        self.calibration_window.hide()
        self.session_window.hide()
        self.patients_window.hide()
        self.login_window.show()

    def show_patients_window(self):
        self.login_window.hide()
        self.calibration_window.hide()
        self.session_window.close()
        self.new_patient_window.hide()
        self.patients_window.show()

    def show_report_window(self):
        # self.login_window.hide()
        self.calibration_window.hide()
        # self.session_window.close()
        # self.new_patient_window.hide()
        self.ReportPage.show()

    def show_calibration_window(self):
        self.patients_window.hide()
        # Setting up the LSLViewer
        self.streams = resolve_stream('type', 'EEG')
        if len(self.streams ) == 0:
            raise(RuntimeError("Can't find EEG stream"))
        # lslv = LSLViewer(self.streams [0], self.calibration_window.fig, self.calibration_window.axes, window=5, scale=891)
        lslv = LSLViewer(self.streams [0], self.calibration_window.fig, self.calibration_window.axes, window=5, scale=57)
        # Start the LSLViewer
        lslv.start()
        self.calibration_window.show()

    def show_session_window(self):
        self.patients_window.hide()
        # Setting up the LSLViewer
        self.streams = resolve_stream('type', 'EEG')
        if len(self.streams ) == 0:
            raise(RuntimeError("Can't find EEG stream"))
        # lslv = LSLViewer(self.streams [0], self.session_ui.fig, self.session_ui.axes, window=5, scale=891)
        lslv = LSLViewer(self.streams [0], self.session_ui.fig, self.session_ui.axes, window=5, scale=57)
        
        # Start the LSLViewer
        lslv.start()

        self.session_window.show()

    def show_new_patient_window(self):
        self.patients_window.hide()
        self.new_patient_window.show()
    
    def start_automation_tasks(self):
        # Extract EEG stream info
        self.automation_window.sfreq, self.automation_window.ch_names = extract_stream_info()
        self.automation_window.setupUi(self.automation_window)
        self.automation_window.show()


    def run(self):
        self.login_window.show()
        self.app.exec_()

if __name__ == "__main__":
    controller = MainController()
    controller.run()
