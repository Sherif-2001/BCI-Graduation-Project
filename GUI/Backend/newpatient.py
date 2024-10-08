# newpatient.py
from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import sys
from PyQt5.QtWidgets import QMessageBox

class NewPatientMainWindow(QtWidgets.QMainWindow):
    go_back = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_NewPatientMainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.on_submit)
        self.ui.pushButton_2.clicked.connect(self.go_back.emit)

class Ui_NewPatientMainWindow(object):
    def setupUi(self, NewPatientMainWindow):
        NewPatientMainWindow.setObjectName("NewPatientMainWindow")
        NewPatientMainWindow.resize(727, 678)
        NewPatientMainWindow.setStyleSheet("background-color:#265073;\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(NewPatientMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 5, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setStyleSheet("background-color:rgb(75, 75, 75);\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 12, 4, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 7, 4, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 21, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 17, 0, 1, 7)
        self.textEdit_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_10.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_10.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.gridLayout.addWidget(self.textEdit_10, 22, 0, 1, 7)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(NewPatientMainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.gridLayout.addWidget(self.radioButton_6, 16, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 3)
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_6.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout.addWidget(self.textEdit_6, 13, 0, 1, 3)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup = QtWidgets.QButtonGroup(NewPatientMainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_3)
        self.gridLayout.addWidget(self.radioButton_3, 16, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 15, 0, 1, 3)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 18, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 4, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 4, 1, 2)
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_7.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout.addWidget(self.textEdit_7, 13, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 4, 1, 2)
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_9.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_9.setObjectName("textEdit_9")
        self.gridLayout.addWidget(self.textEdit_9, 19, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 18, 4, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 7)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#2D9596;\n"
"border-radius:5%;\n"
"color:rgb(255, 255, 255);\n"
"font: 20pt \"Forte\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(67, 183, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 24, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 14, 0, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 7)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 11, 0, 1, 7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 23, 0, 1, 7)
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setMinimumSize(QtCore.QSize(87, 30))
        self.textEdit_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_8.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout.addWidget(self.textEdit_8, 13, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(120,120, 120);\n"
"border-radius:15;\n"
"color:rgb(255, 255, 255);\n"
"font: 25pt \"Forte\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(70, 70, 70);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 24, 0, 1, 1)
        self.pushButton.clicked.connect(self.on_submit)

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.gridLayout.addWidget(self.radioButton_4, 16, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("background-color:rgb(75, 75, 75);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 19, 4, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 20, 0, 1, 7)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup_2.addButton(self.radioButton_5)
        self.gridLayout.addWidget(self.radioButton_5, 16, 5, 1, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 5, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 7)
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 7, 0, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 15, 4, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 3)
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_5.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0,0,0);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout.addWidget(self.textEdit_5, 10, 0, 1, 7)
        NewPatientMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewPatientMainWindow)
        self.statusbar.setObjectName("statusbar")
        NewPatientMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewPatientMainWindow)
        QtCore.QMetaObject.connectSlotsByName(NewPatientMainWindow)

    def retranslateUi(self, NewPatientMainWindow):
        _translate = QtCore.QCoreApplication.translate
        NewPatientMainWindow.setWindowTitle(_translate("NewPatientMainWindow", "New Patient"))
        self.label_10.setText(_translate("NewPatientMainWindow", "Weight:"))
        self.label_9.setText(_translate("NewPatientMainWindow", "Height:"))
        self.label_14.setText(_translate("NewPatientMainWindow", "Notes:"))
        self.radioButton_6.setText(_translate("NewPatientMainWindow", "Right"))
        self.label_8.setText(_translate("NewPatientMainWindow", "National ID:"))
        self.radioButton_3.setText(_translate("NewPatientMainWindow", "Right"))
        self.label_11.setText(_translate("NewPatientMainWindow", "Dominant Hand:"))
        self.label_13.setText(_translate("NewPatientMainWindow", "Disease:"))
        self.label_4.setText(_translate("NewPatientMainWindow", "Gender:"))
        self.label_6.setText(_translate("NewPatientMainWindow", "Mobile Number:"))
        self.label.setText(_translate("NewPatientMainWindow", "First Name:"))
        self.radioButton.setText(_translate("NewPatientMainWindow", "Male"))
        self.label_15.setText(_translate("NewPatientMainWindow", "Object Shape:"))
        self.pushButton.setText(_translate("NewPatientMainWindow", "Submit"))
        self.label_3.setText(_translate("NewPatientMainWindow", "Date of Birth:"))
        self.label_7.setText(_translate("NewPatientMainWindow", "Adress:"))
        self.pushButton_2.setText(_translate("NewPatientMainWindow", "Back"))
        self.radioButton_4.setText(_translate("NewPatientMainWindow", "Left"))
        self.comboBox.setItemText(0, _translate("NewPatientMainWindow", "Ball"))
        self.comboBox.setItemText(1, _translate("NewPatientMainWindow", "Bottle"))
        self.comboBox.setItemText(2, _translate("NewPatientMainWindow", "Pen"))
        self.comboBox.setItemText(3, _translate("NewPatientMainWindow", "Key"))
        self.label_2.setText(_translate("NewPatientMainWindow", "Last Name:"))
        self.radioButton_5.setText(_translate("NewPatientMainWindow", "Left"))
        self.radioButton_2.setText(_translate("NewPatientMainWindow", "Female"))
        self.label_5.setText(_translate("NewPatientMainWindow", "Phone Number:"))
        self.label_12.setText(_translate("NewPatientMainWindow", "Affacted Hand:"))

    def on_submit(self):
        # Collect data from the UI
        first_name = self.textEdit.toPlainText()
        last_name = self.textEdit_2.toPlainText()
        dob = self.dateEdit.date().toString("dd/MM/yyyy")
        gender = (
            "Male"
            if self.radioButton.isChecked()
            else "Female" if self.radioButton_2.isChecked() else ""
        )
        phone_number = self.textEdit_3.toPlainText()
        mobile_number = self.textEdit_4.toPlainText()
        address = self.textEdit_5.toPlainText()
        national_id = self.textEdit_6.toPlainText()
        height = self.textEdit_7.toPlainText()
        weight = self.textEdit_8.toPlainText()
        dominant_hand = (
            "Right"
            if self.radioButton_3.isChecked()
            else "Left" if self.radioButton_4.isChecked() else ""
        )
        affected_hand = (
            "Right"
            if self.radioButton_6.isChecked()
            else "Left" if self.radioButton_5.isChecked() else ""
        )
        disease = self.textEdit_9.toPlainText()
        object_shape = self.comboBox.currentText()

        # Create full name
        full_name = first_name + " " + last_name

        # Create a new Patient instance
        new_patient = Patient(
            name=full_name,
            dob=dob,
            gender=gender,
            phone_number=phone_number,
            mobile_number=mobile_number,
            address=address,
            national_id=national_id,
            height=height,
            weight=weight,
            dominant_hand=dominant_hand,
            affected_hand=affected_hand,
            disease=disease,
            object_shape=object_shape,
        )
        try:
            new_patient.upload_patient_to_firebase()
            print("New Patient Added")
            # self.go_to_main()
            QMessageBox.information(
                self.centralwidget,
                "Patient Added",
                f"Patient {first_name} is added successfully!",
            )
        except Exception as e:
            # QMessageBox.warning(self.LoginPageMainWindow, "Error", str(e))
            QMessageBox.warning(self.centralwidget, "Error", "Invalid Input")


class Patient:
    def __init__(
        self,
        name,
        dob,
        gender,
        phone_number,
        mobile_number,
        address,
        national_id,
        height,
        weight,
        dominant_hand,
        affected_hand,
        disease,
        object_shape,
    ):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.mobile_number = mobile_number
        self.address = address
        self.national_id = national_id
        self.height = height
        self.weight = weight
        self.dominant_hand = dominant_hand
        self.affected_hand = affected_hand
        self.disease = disease
        self.object_shape = object_shape
        self.reports = []

    def to_dict(self):
        return {
            "Name": self.name,
            "DOB": self.dob,
            "Gender": self.gender,
            "PhoneNum": self.phone_number,
            "MobileNum": self.mobile_number,
            "Address": self.address,
            "NationalId": self.national_id,
            "Height": self.height,
            "Weight": self.weight,
            "DominantHand": self.dominant_hand,
            "AffectedHand": self.affected_hand,
            "Disease": self.disease,
            "ObjectShape": self.object_shape,
            "reports": [report.to_dict() for report in self.reports],
        }

    def upload_patient_to_firebase(self):
        config = {
            "apiKey": "AIzaSyBaf2PZ9lRnkpM952pBDlfGCxxEjcvU4Bk",
            "authDomain": "fes-controller.firebaseapp.com",
            "databaseURL": "https://fes-controller-default-rtdb.firebaseio.com",
            "projectId": "fes-controller",
            "storageBucket": "fes-controller.appspot.com",
            "messagingSenderId": "341771619246",
            "appId": "1:341771619246:web:29d7cc61c889b3228a163f",
        }

        # Initialize Firebase
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()

        db.child("patients").child(self.name).set(self.to_dict())


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    NewPatientMainWindow = QtWidgets.QMainWindow()
    ui = Ui_NewPatientMainWindow()
    ui.setupUi(NewPatientMainWindow)
    NewPatientMainWindow.show()
    sys.exit(app.exec_())
