# patients.py

from PyQt5 import QtWidgets, QtCore
from newpatient import NewPatientMainWindow

class PatientsMainWindow(QtWidgets.QMainWindow):
    go_back = QtCore.pyqtSignal()
    open_calibration = QtCore.pyqtSignal()
    open_session = QtCore.pyqtSignal()
    open_new_patient = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_PatientsMainWindow()
        self.ui.setupUi(self)
        self.ui.menuBack.triggered.connect(self.go_back.emit)
        self.ui.pushButton_3.clicked.connect(self.open_calibration.emit)
        self.ui.pushButton_2.clicked.connect(self.open_session.emit)
        self.ui.pushButton.clicked.connect(self.open_new_patient.emit)

class Ui_PatientsMainWindow(object):
    def setupUi(self, PatientsMainWindow):
        PatientsMainWindow.setObjectName("PatientsMainWindow")
        PatientsMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PatientsMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 200, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 250, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        PatientsMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PatientsMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuBack = QtWidgets.QMenu(self.menubar)
        self.menuBack.setObjectName("menuBack")
        PatientsMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PatientsMainWindow)
        self.statusbar.setObjectName("statusbar")
        PatientsMainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuBack.menuAction())

        self.retranslateUi(PatientsMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PatientsMainWindow)

    def retranslateUi(self, PatientsMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PatientsMainWindow.setWindowTitle(_translate("PatientsMainWindow", "MainWindow"))
        self.pushButton.setText(_translate("PatientsMainWindow", "New Patient"))
        self.pushButton_2.setText(_translate("PatientsMainWindow", "Session"))
        self.pushButton_3.setText(_translate("PatientsMainWindow", "Calibration"))
        self.menuBack.setTitle(_translate("PatientsMainWindow", "Back"))
