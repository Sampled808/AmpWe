#!/usr/bin/env python3
from PyQt5.QtWidgets import *
import sys
import signup

# creating a class
# that inherits the QDialog class
class LoginWindow(QDialog):

    # constructor
    def __init__(self):
        super(LoginWindow, self).__init__()


        # setting window title
        self.setWindowTitle("AmpWe")

        # setting geometry to the window
        self.setGeometry(100, 100, 300, 400)

        # creating a group box
        self.formGroupBox = QGroupBox("Log In")


        # creating a line edit for username
        self.nameLineEdit = QLineEdit()


        self.PasswordLineEdit = QLineEdit()
        self.PasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.SignUpButton = QPushButton('Sign Up')
        self.SignUpButton.clicked.connect(self.signup_layout)
        # calling the method that create the form
        layout = self.createForm()

        # Setting the layout
        self.formGroupBox.setLayout(layout)
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)

        # addding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting layout
        self.setLayout(mainLayout)

    def signup_layout(self, *args):
        signup.Ui_RegisterForm().exec()

    # get info method called when form is accepted
    def getInfo(self):

        # printing the form information
        print("Person Name : {0}".format(self.nameLineEdit.text()))

        # closing the window
        self.close()

    # creat form method
    def createForm(self):

        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and password
        layout.addRow(QLabel("Username"), self.nameLineEdit)
        layout.addRow(QLabel("Password"), self.PasswordLineEdit)
        layout.addRow(self.SignUpButton)
        return layout

# main method
if __name__ == '__main__':

    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = LoginWindow()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())

