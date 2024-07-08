from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainPageMainWindow
import pyrebase


class Ui_LoginPageMainWindow(object):
    def setupUi(self, LoginPageMainWindow):
        LoginPageMainWindow.setObjectName("LoginPageMainWindow")
        LoginPageMainWindow.resize(727, 662)
        self.centralwidget = QtWidgets.QWidget(LoginPageMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(
            "background-color:#265073;\n"
            "color:rgb(255, 255, 255);\n"
            "border-radius:10px;"
        )
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet('font: 700 80pt "Agency FB";')
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(
            280, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem2)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(
            50, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_6.addWidget(self.textEdit_2)
        self.loginButton = QtWidgets.QPushButton("Login", self.widget_3)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 30))
        self.verticalLayout_6.addWidget(self.loginButton)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_3.addWidget(self.widget_3)
        spacerItem5 = QtWidgets.QSpacerItem(
            280, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_5.addWidget(self.widget_2)
        LoginPageMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPageMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 22))
        self.menubar.setObjectName("menubar")
        LoginPageMainWindow.setMenuBar(self.menubar)

        self.retranslateUi(LoginPageMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginPageMainWindow)

    def retranslateUi(self, LoginPageMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginPageMainWindow.setWindowTitle(_translate("LoginPageMainWindow", "Log In"))
        self.label.setText(_translate("LoginPageMainWindow", "HandNeuro"))
        self.label_3.setText(_translate("LoginPageMainWindow", "Email:"))
        self.label_2.setText(_translate("LoginPageMainWindow", "Password:"))


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class LoginPage(QtWidgets.QMainWindow, Ui_LoginPageMainWindow):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.go_to_main)

    def go_to_main(self):
        self.main_window = MainPage()
        self.main_window.show()
        self.close()

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            self.go_to_main()
            print("Login Successful!!")
        except Exception as e:
            print("Error: ", str(e))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginPageMainWindow = LoginPage()
    LoginPageMainWindow.show()
    sys.exit(app.exec_())
