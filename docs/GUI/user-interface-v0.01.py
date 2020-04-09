from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QComboBox, QVBoxLayout, QHBoxLayout 
from PyQt5.QtGui import QIcon, QPixmap
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
       
        # Initialize window:
        self.setWindowTitle("OpenCARGO Desktop App")
        self.setFixedSize(640,480)
        # --------------------
        
        
        # Initialize tabs:
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab1,"Staff Login")
        self.tabs.addTab(self.tab2,"Track")
        self.tabs.addTab(self.tab3,"Create a Shipment")
        self.tabs.addTab(self.tab4,"Services")
        self.tabs.addTab(self.tab5,"Info")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        # -------------------------
        
        
        # Initialize 1st tab (Staff login):
        self.tab1.pixmap = QPixmap('icon.png')
        self.tab1.logo = QLabel()
        self.tab1.logo.setPixmap(self.tab1.pixmap)
        
        self.tab1.label1 = QLabel("Username:")
        self.tab1.edit1 = QLineEdit()
        
        self.tab1.label2 = QLabel("Password:")
        self.tab1.edit2 = QLineEdit()
        self.tab1.edit2.setEchoMode(QLineEdit.Password)
        
        self.tab1.check = QCheckBox("Stay logged in")
        
        self.tab1.button = QPushButton("Login")
        self.tab1.hbox = QHBoxLayout()
        self.tab1.vbox = QVBoxLayout()
        self.tab1.vbox.addWidget(self.tab1.logo)
        self.tab1.vbox.addWidget(self.tab1.label1)
        self.tab1.vbox.addWidget(self.tab1.edit1)
        self.tab1.vbox.addWidget(self.tab1.label2)
        self.tab1.vbox.addWidget(self.tab1.edit2)
        self.tab1.vbox.addWidget(self.tab1.check)
        self.tab1.vbox.addWidget(self.tab1.button)
        self.tab1.vbox.addStretch()
        self.tab1.hbox.addStretch()
        self.tab1.hbox.addLayout(self.tab1.vbox)
        self.tab1.hbox.addStretch()
        self.tab1.setLayout(self.tab1.hbox)
        # ---------------------------------
        
        
        # Initialize 2nd tab (Tracking):
        self.tab2.label1 = QLabel("Enter your tracking number:")
        self.tab2.edit1 = QTextEdit()
        self.tab2.button = QPushButton("Track")
        
        self.tab2.vbox = QVBoxLayout()
        self.tab2.vbox.addStretch()
        self.tab2.vbox.addWidget(self.tab2.label1)
        self.tab2.vbox.addWidget(self.tab2.edit1)
        self.tab2.vbox.addWidget(self.tab2.button)
        self.tab2.hbox = QHBoxLayout()
        self.tab2.hbox.addLayout(self.tab2.vbox)
        self.tab2.setLayout(self.tab2.hbox)
        # ---------------------------------
        
        
        # Initialize 3rd tab (Services):
        self.tab3.label1 = QLabel("Full name of sender:")
        self.tab3.edit1 = QLineEdit()
        
        self.tab3.label2 = QLabel("Contact number or e-mail adress of sender:")
        self.tab3.edit2 = QLineEdit()
        
        self.tab3.label3 = QLabel("Adress of sender:")
        self.tab3.edit3 = QLineEdit()
        
        self.tab3.label4 = QLabel("Full name of recipient:")
        self.tab3.edit4 = QLineEdit()
        
        self.tab3.label5 = QLabel("Contact number or e-mail adress of recipient:")
        self.tab3.edit5 = QLineEdit()
        
        self.tab3.label6 = QLabel("Adress to be delivered:") 
        self.tab3.edit6 = QLineEdit()
        
        self.tab3.label7 = QLabel("Weight (kg) of package:")
        self.tab3.edit7 = QLineEdit()
        
        self.tab3.label8 = QLabel("Volume (L) of package:")
        self.tab3.edit8 = QLineEdit()
        
        self.tab3.label9 = QLabel("Senstive package:")
        self.tab3.edit9 = QCheckBox()
        
        self.tab3.button = QPushButton("Submit")
        
        self.tab3.vbox = QVBoxLayout()
        self.tab3.hbox = QHBoxLayout()
        self.tab3.vbox.addWidget(self.tab3.label1)
        self.tab3.vbox.addWidget(self.tab3.edit1)
        self.tab3.vbox.addWidget(self.tab3.label2)
        self.tab3.vbox.addWidget(self.tab3.edit2)
        self.tab3.vbox.addWidget(self.tab3.label3)
        self.tab3.vbox.addWidget(self.tab3.edit3)
        self.tab3.vbox.addWidget(self.tab3.label4)
        self.tab3.vbox.addWidget(self.tab3.edit4)
        self.tab3.vbox.addWidget(self.tab3.label5)
        self.tab3.vbox.addWidget(self.tab3.edit5)
        self.tab3.vbox.addWidget(self.tab3.label6)
        self.tab3.vbox.addWidget(self.tab3.edit6)
        self.tab3.vbox.addWidget(self.tab3.label7)
        self.tab3.vbox.addWidget(self.tab3.edit7)
        self.tab3.vbox.addWidget(self.tab3.label8)
        self.tab3.vbox.addWidget(self.tab3.edit8)
        self.tab3.vbox.addWidget(self.tab3.label9)
        self.tab3.vbox.addWidget(self.tab3.edit9)
        self.tab3.vbox.addWidget(self.tab3.button)
        self.tab3.hbox.addLayout(self.tab3.vbox)
        self.tab3.setLayout(self.tab3.hbox)
        # ---------------------------------
        
        self.show()


app = QApplication(sys.argv)
    
win1 = Window()
 
sys.exit(app.exec_())