import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("User Login")
        
        self.label_user = QtWidgets.QLabel("Username:")
        self.input_user = QtWidgets.QLineEdit()
        self.label_pass = QtWidgets.QLabel("Password:")
        self.input_pass = QtWidgets.QLineEdit()
        self.input_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.stay_logged = QtWidgets.QCheckBox("Stay logged in")
        self.message = QtWidgets.QLabel("")
        self.button = QtWidgets.QPushButton("Login")
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.label_user)
        vbox.addWidget(self.input_user)
        vbox.addWidget(self.label_pass)
        vbox.addWidget(self.input_pass)
        vbox.addWidget(self.stay_logged)
        vbox.addWidget(self.message)
        vbox.addWidget(self.button)
        vbox.addStretch()
        self.setLayout(vbox)
        
        self.button.clicked.connect(self.login)
        
        self.show()
    
    def login(self):
        user = self.input_user.text()
        password = self.input_pass.text()
        for i in range(2):
            if usernames[i] == user and passwords[i] == password:
                self.message.setText("User logged in.")
            else:
                self.message.setText("Invalid username-password combination.")
        
usernames = ["byerlikaya45","abarisyerlikaya"]
passwords = ["123456","4504fb"]
        
app = QtWidgets.QApplication(sys.argv)

win = Window()

sys.exit(app.exec_())        