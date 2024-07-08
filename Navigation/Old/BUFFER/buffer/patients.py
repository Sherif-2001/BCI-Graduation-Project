from PyQt5 import QtCore, QtGui, QtWidgets

class PatientsMainWindow(QtWidgets.QMainWindow):
    go_back = QtCore.pyqtSignal()
    go_to_calibration = QtCore.pyqtSignal()
    go_to_session = QtCore.pyqtSignal()
    go_to_new_patient = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_PatientsMainWindow()
        self.ui.setupUi(self)
        self.ui.menuBack.triggered.connect(self.go_back.emit)
        self.ui.pushButton_3.clicked.connect(self.go_to_calibration.emit)
        self.ui.pushButton_2.clicked.connect(self.go_to_session.emit)

        self.ui.pushButton.clicked.connect(self.go_to_new_patient.emit)


class Ui_PatientsMainWindow(object):
    def setupUi(self, PatientsMainWindow):
        PatientsMainWindow.setObjectName("PatientsMainWindow")
        PatientsMainWindow.resize(727, 662)
        PatientsMainWindow.setStyleSheet("background-color:#265073;\n"
                                         "color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(PatientsMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 14, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 13, 0, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 14, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 8, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 12, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 13, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:#2D9596;\n"
                                      "border-radius:5%;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "font: 25pt \"Forte\";\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:rgb(67, 183, 255);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 8, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("background-color:rgb(75, 75, 75);\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "font: 18pt ;\n"
                                    "")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 8)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 10, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 9, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 12, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 11, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "font: 12pt ;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 11, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 10, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font: 12pt ;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 9, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 12pt ;")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(207, 0, 3);\n"
                                        "border-radius:5%;\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "font: 25pt \"Forte\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color:rgb(239, 0, 0);\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(207, 0, 3);\n"
                                        "border-radius:5%;\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "font: 25pt \"Forte\";\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color:rgb(239, 0, 0);\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout, 14, 8, 1, 1)
        PatientsMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PatientsMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 38))
        self.menubar.setStyleSheet("QMenuBar {\n"
                                   "    color:rgb(255, 255, 255);\n"
                                   "    font: 585 15pt; \n"
                                   "}\n"
                                   "QMenuBar::item {\n"
                                   "    background-color: #444444;\n"
                                   "    color: white;\n"
                                   "    padding: 5px 10px;\n"
                                   "}\n"
                                   "QMenuBar::item:selected { /* when mouse hover */\n"
                                   "    background-color: #A9A9A9;\n"
                                   "}\n"
                                   "")
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
        PatientsMainWindow.setWindowTitle(_translate("PatientsMainWindow", "Patients"))
        self.label_11.setText(_translate("PatientsMainWindow", "Mobile Number:"))
        self.label_28.setText(_translate("PatientsMainWindow", "Object Shape:"))
        self.label_10.setText(_translate("PatientsMainWindow", "Phone number"))
        self.label_22.setText(_translate("PatientsMainWindow", "Disease:"))
        self.label_27.setText(_translate("PatientsMainWindow", "Object Shape"))
        self.label_9.setText(_translate("PatientsMainWindow", "Phone number:"))
        self.label_16.setText(_translate("PatientsMainWindow", "National ID"))
        self.label_4.setText(_translate("PatientsMainWindow", "ID"))
        self.label_24.setText(_translate("PatientsMainWindow", "Affected Hand:"))
        self.label_2.setText(_translate("PatientsMainWindow", "Patient ID:"))
        self.label_18.setText(_translate("PatientsMainWindow", "Disease"))
        self.pushButton.setText(_translate("PatientsMainWindow", "New Patient"))
        self.label_7.setText(_translate("PatientsMainWindow", "Gender:"))
        self.label_3.setText(_translate("PatientsMainWindow", "Name"))
        self.label_23.setText(_translate("PatientsMainWindow", "Weight"))
        self.label_12.setText(_translate("PatientsMainWindow", "Mobile Number"))
        self.label_25.setText(_translate("PatientsMainWindow", "Height"))
        self.label_26.setText(_translate("PatientsMainWindow", "Affected Hand"))
        self.label_20.setText(_translate("PatientsMainWindow", "Dominant Hand"))
        self.label_8.setText(_translate("PatientsMainWindow", "Gender"))
        self.label.setText(_translate("PatientsMainWindow", "Patient Name:"))
        self.label_21.setText(_translate("PatientsMainWindow", "Dominant Hand:"))
        self.label_6.setText(_translate("PatientsMainWindow", "Age"))
        self.label_17.setText(_translate("PatientsMainWindow", "Weight:"))
        self.label_5.setText(_translate("PatientsMainWindow", "Age:"))
        self.label_15.setText(_translate("PatientsMainWindow", "National ID:"))
        self.label_14.setText(_translate("PatientsMainWindow", "Address"))
        self.label_19.setText(_translate("PatientsMainWindow", "Height:"))
        self.label_13.setText(_translate("PatientsMainWindow", "Address:"))
        self.pushButton_3.setText(_translate("PatientsMainWindow", "Rehab Session"))
        self.pushButton_2.setText(_translate("PatientsMainWindow", "EEG Session"))
        self.menuBack.setTitle(_translate("PatientsMainWindow", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatientsMainWindow = PatientsMainWindow()
    PatientsMainWindow.show()
    sys.exit(app.exec_())
