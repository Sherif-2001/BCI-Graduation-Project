from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainPageMainWindow(object):
    def setupUi(self, MainPageMainWindow):
        MainPageMainWindow.setObjectName("MainPageMainWindow")
        MainPageMainWindow.resize(727, 662)
        MainPageMainWindow.setStyleSheet("background-color:#265073;\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainPageMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color:#2D9596;\n"
"font: 700 20pt \"Agency FB\";\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#9AD0C2;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 700 80pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color:#2D9596;\n"
"font: 700 20pt \"Agency FB\";\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#9AD0C2;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color:#2D9596;\n"
"font: 700 20pt \"Agency FB\";\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#9AD0C2;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:#2D9596;\n"
"font: 700 20pt \"Agency FB\";\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#9AD0C2;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        MainPageMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainPageMainWindow)
        self.statusbar.setObjectName("statusbar")
        MainPageMainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainPageMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 727, 38))
        self.menuBar.setStyleSheet("QMenuBar {\n"
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
        self.menuBar.setObjectName("menuBar")
        self.menuBack = QtWidgets.QMenu(self.menuBar)
        self.menuBack.setStyleSheet("")
        self.menuBack.setObjectName("menuBack")
        MainPageMainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuBack.menuAction())

        self.retranslateUi(MainPageMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainPageMainWindow)

    def retranslateUi(self, MainPageMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainPageMainWindow.setWindowTitle(_translate("MainPageMainWindow", "Main"))
        self.pushButton_4.setText(_translate("MainPageMainWindow", "FES Calibration"))
        self.label.setText(_translate("MainPageMainWindow", "HandNeuro"))
        self.pushButton_3.setText(_translate("MainPageMainWindow", "Report"))
        self.pushButton_5.setText(_translate("MainPageMainWindow", "Glove Calibration"))
        self.pushButton_2.setText(_translate("MainPageMainWindow", "Patients"))
        self.menuBack.setTitle(_translate("MainPageMainWindow", "Back"))


class MainPage(QtWidgets.QMainWindow, Ui_MainPageMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        self.setupUi(self)
        self.menuBack.triggered.connect(self.go_to_login)

    def go_to_login(self):
        self.login_window = LoginPage()
        self.login_window.show()
        self.close()


if __name__ == "__main__":
    import sys
    from login import LoginPage
    app = QtWidgets.QApplication(sys.argv)
    MainPageMainWindow = MainPage()
    MainPageMainWindow.show()
    sys.exit(app.exec_())
