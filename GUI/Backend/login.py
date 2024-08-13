# login.py
from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
from PyQt5.QtWidgets import QMessageBox

class LoginPageMainWindow(QtWidgets.QMainWindow):
    login_successful = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginPageMainWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)

    def login(self):
        config = {
            "apiKey": "AIzaSyBaf2PZ9lRnkpM952pBDlfGCxxEjcvU4Bk",
            "authDomain": "fes-controller.firebaseapp.com",
            "databaseURL": "https://fes-controller-default-rtdb.firebaseio.com",
            "projectId": "fes-controller",
            "storageBucket": "fes-controller.appspot.com",
            "messagingSenderId": "341771619246",
            "appId": "1:341771619246:web:29d7cc61c889b3228a163f",
        }

        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        email = self.ui.email_field.toPlainText()
        password = self.ui.password_field.toPlainText()

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            print("Login Successful!!")
            # Notify the main controller about successful login
            self.login_successful.emit()
            # QMessageBox.information(self, "Success", "Sign In successful!")
        except Exception as e:
            QMessageBox.warning(self, "Error", "Please Enter Valid Email and Password")
            print("Error: ", str(e))

class Ui_LoginPageMainWindow(object):
    def setupUi(self, LoginPageMainWindow):
        LoginPageMainWindow.setObjectName("LoginPageMainWindow")
        LoginPageMainWindow.resize(727, 662)
        self.centralwidget = QtWidgets.QWidget(LoginPageMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color:#265073;\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 700 80pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(280, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(50, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.email_field = QtWidgets.QTextEdit(self.widget_3)
        self.email_field.setMinimumSize(QtCore.QSize(0, 30))
        self.email_field.setObjectName("email_field")
        self.verticalLayout_2.addWidget(self.email_field)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.password_field = QtWidgets.QTextEdit(self.widget_3)
        self.password_field.setMinimumSize(QtCore.QSize(0, 30))
        self.password_field.setObjectName("password_field")
        self.verticalLayout.addWidget(self.password_field)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.loginButton = QtWidgets.QPushButton(self.widget_3)
        self.loginButton.setStyleSheet("QPushButton{\n"
"background-color:#2D9596;\n"
"border-radius:5%;\n"
"color:rgb(255, 255, 255);\n"
"font: 20pt \"Forte\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(67, 183, 255);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_6.addWidget(self.loginButton)

        self.horizontalLayout_3.addWidget(self.widget_3)
        spacerItem5 = QtWidgets.QSpacerItem(280, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.loginButton.setText(_translate("LoginPageMainWindow", "Login"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPageMainWindow = LoginPageMainWindow()
    LoginPageMainWindow.show()
    sys.exit(app.exec_())
