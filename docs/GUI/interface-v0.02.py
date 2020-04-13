import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QTextEdit, QCheckBox, QLineEdit, QPushButton, \
    QCheckBox, QComboBox, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,QGroupBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
class Success(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text = QLabel("\n     Succeed")
        self.but = QPushButton("Ok")
        self.setWindowIcon(QIcon('icon2.png'))
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.text)
        self.vbox.addStretch()
        self.vbox.addWidget(self.but)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch()
        self.setLayout(self.hbox)
        self.setGeometry(900,400,150,100)
        self.show()
        self.but.clicked.connect(self.exit)
    def exit(self):
        self.hide()


class StaffW(QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti()
        self.init_ui()

    def baglanti(self):
        baglan = sqlite3.connect("database_staff.db")

        self.cursor = baglan.cursor()

        self.cursor.execute("Create Table If not exists staff_list (Username TEXT,Password TEXT)")

        baglan.commit()

    def init_ui(self):

        self.setWindowTitle("Staff Login")
        self.setWindowIcon(QIcon('icon2.png'))
        self.pixmap = QPixmap('icon.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.pixmap)
        self.move(800,250)
        self.yazi1 = QLabel("Username")
        self.user = QLineEdit()
        self.user.setFixedWidth(250)

        self.yazi2 = QLabel("Password")
        self.passw = QLineEdit()
        self.passw.setEchoMode(QLineEdit.Password)
        self.passw.setFixedWidth(250)

        self.button = QPushButton("Sign In")
        self.button.setFixedWidth(250)
        self.button.setFixedHeight(50)
        self.yazi3 = QLabel(" ")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.logo)
        self.vbox.addWidget(self.yazi1)
        self.vbox.addWidget(self.user)
        self.vbox.addWidget(self.yazi2)
        self.vbox.addWidget(self.passw)
        self.vbox.addWidget(self.yazi3)
        self.vbox.addStretch()
        self.vbox.addWidget(self.button)
        self.button.clicked.connect(self.staffcheck)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch()

        self.setLayout(self.hbox)

        self.show()

    def staffcheck(self):
        name = self.user.text()
        pasw = self.passw.text()

        self.cursor.execute("Select * From staff_list where Username = ? and Password = ?", (name, pasw))

        data = self.cursor.fetchall()
        if len(data) == 0:
            self.yazi3.setText("Wrong Username or Password.")
        else:
            self.staffLogin()

    def staffLogin(self):
        self.win2 = QWidget()
        self.layout2 = QVBoxLayout()
        self.table1 = Table()
        self.layout2.addWidget(self.table1)
        self.win2.setLayout(self.layout2)
        self.win2.show()
        self.hide()


class Opening(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Initialize window:
        self.setWindowTitle("OpenCARGO")
        self.setWindowIcon(QIcon('icon2.png'))
        self.setFixedSize(540, 480)
        self.pixmap = QPixmap('icon.png')
        self.logo = QLabel()
        self.logo.setPixmap(self.pixmap)
        self.user = QPushButton("User Login")
        self.user.setFixedHeight(120)
        self.user.setFixedWidth(120)
        self.button = QPushButton("Staff Login")
        self.button.setFixedWidth(120)
        self.button.setFixedHeight(120)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.vbox.addWidget(self.logo)
        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch()
        self.hbox2.addWidget(self.user)
        self.hbox2.addWidget(self.button)
        self.hbox2.addStretch()
        self.vbox.addLayout(self.hbox2)
        self.vbox.addStretch()
        self.hbox.addStretch()
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch()
        self.setLayout(self.hbox)
        self.show()

        self.user.clicked.connect(self.userlogin)
        self.button.clicked.connect(self.staffLoginFirst)

    def staffLoginFirst(self):
        self.window = StaffW()
        self.window.show()
        self.hide()

    def userlogin(self):
        self.window = Window()
        self.window.show()
        self.hide()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Initialize window:
        self.setWindowTitle("OpenCARGO ")
        self.setFixedSize(640, 480)
        self.setWindowIcon(QIcon('icon2.png'))
        # --------------------

        # Initialize tabs:
        self.tabs = QTabWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab2, "Services")
        self.tabs.addTab(self.tab3, "Create a Shipment")
        self.tabs.addTab(self.tab4, "Info")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        # -------------------------

        # Initialize 2nd tab (Services):
        # Tracking:
        self.tab2.label1 = QLabel("Enter your tracking number:")
        self.tab2.edit1 = QLineEdit()
        self.tab2.edit1.setPlaceholderText("XXXX-XXXX-XXXX")
        self.tab2.button1 = QPushButton("Track")
        self.tab2.vbox1 = QVBoxLayout()
        self.tab2.vbox1.addStretch()
        self.tab2.vbox1.addWidget(self.tab2.label1)
        self.tab2.vbox1.addWidget(self.tab2.edit1)
        self.tab2.vbox1.addWidget(self.tab2.button1)
        self.tab2.vbox1.addStretch()
        self.tab2.hbox1 = QHBoxLayout()
        self.tab2.hbox1.addStretch()
        self.tab2.hbox1.addLayout(self.tab2.vbox1)
        self.tab2.hbox1.addStretch()
        self.tab2.gr1 = QGroupBox("Track Your Shipment")
        self.tab2.gr1.setLayout(self.tab2.hbox1)

        # Price Calculation:
        self.tab2.label3 = QLabel("Weight (kg) of package:")
        self.tab2.edit3 = QLineEdit()
        self.tab2.label4 = QLabel("Volume (L) of package:")
        self.tab2.edit4 = QLineEdit()
        self.tab2.label6 = QLabel("City to depart from:")
        self.tab2.edit6 = QLineEdit()
        self.tab2.label7 = QLabel("City to deliver:")
        self.tab2.edit7 = QLineEdit()
        self.tab2.button4 = QPushButton("Calculate Price")

        self.tab2.vbox2 = QVBoxLayout()
        self.tab2.vbox2.addStretch()
        self.tab2.vbox2.addWidget(self.tab2.label3)
        self.tab2.vbox2.addWidget(self.tab2.edit3)
        self.tab2.vbox2.addWidget(self.tab2.label4)
        self.tab2.vbox2.addWidget(self.tab2.edit4)
        self.tab2.vbox2.addStretch()

        self.tab2.vbox2b = QVBoxLayout()
        self.tab2.vbox2b.addStretch()
        self.tab2.vbox2b.addWidget(self.tab2.label6)
        self.tab2.vbox2b.addWidget(self.tab2.edit6)
        self.tab2.vbox2b.addWidget(self.tab2.label7)
        self.tab2.vbox2b.addWidget(self.tab2.edit7)
        self.tab2.vbox2b.addStretch()

        self.tab2.hbox2 = QHBoxLayout()
        self.tab2.hbox2.addStretch()
        self.tab2.hbox2.addLayout(self.tab2.vbox2)
        self.tab2.hbox2.addLayout(self.tab2.vbox2b)
        self.tab2.hbox2.addStretch()
        self.tab2.hbox2b = QHBoxLayout()
        self.tab2.hbox2b.addStretch()
        self.tab2.hbox2b.addWidget(self.tab2.button4)
        self.tab2.hbox2b.addStretch()
        self.tab2.layout = QVBoxLayout()
        self.tab2.layout.addLayout(self.tab2.hbox2)
        self.tab2.layout.addLayout(self.tab2.hbox2b)
        self.tab2.gr2 = QGroupBox("Calculate Price")
        self.tab2.gr2.setLayout(self.tab2.layout)

        # Contact Us:
        self.tab2.label5 = QLabel("We are here to help you. Please explain your issue briefly:")
        self.tab2.edit5 = QTextEdit()
        self.tab2.button5 = QPushButton("Send")
        self.tab2.vbox3 = QVBoxLayout()
        self.tab2.vbox3.addStretch()
        self.tab2.vbox3.addWidget(self.tab2.label5)
        self.tab2.vbox3.addWidget(self.tab2.edit5)
        self.tab2.vbox3.addWidget(self.tab2.button5)
        self.tab2.vbox3.addStretch()
        self.tab2.hbox3 = QHBoxLayout()
        self.tab2.hbox3.addStretch()
        self.tab2.hbox3.addLayout(self.tab2.vbox3)
        self.tab2.hbox3.addStretch()
        self.tab2.gr3 = QGroupBox()
        self.tab2.gr3 = QGroupBox("Contact Us")
        self.tab2.gr3.setLayout(self.tab2.hbox3)

        # Layout:
        self.tab2.layout = QVBoxLayout()
        self.tab2.layout.addWidget(self.tab2.gr1)
        self.tab2.layout.addWidget(self.tab2.gr2)
        self.tab2.layout.addWidget(self.tab2.gr3)
        self.tab2.setLayout(self.tab2.layout)
        # ---------------------------------

        # Initialize 3rd tab (Services):
        self.tab3.label1 = QLabel("Full name of sender:")
        self.tab3.edit1 = QLineEdit()

        self.tab3.label2 = QLabel("Contact number of sender:")
        self.tab3.edit2 = QLineEdit()

        self.tab3.label3 = QLabel("Adress of sender:")
        self.tab3.edit3 = QLineEdit()

        self.tab3.label4 = QLabel("Full name of recipient:")
        self.tab3.edit4 = QLineEdit()

        self.tab3.label5 = QLabel("Contact number of recipient:")
        self.tab3.edit5 = QLineEdit()

        self.tab3.label6 = QLabel("Adress to be delivered:")
        self.tab3.edit6 = QLineEdit()

        self.tab3.label7 = QLabel("Weight (kg) of package:")
        self.tab3.edit7 = QLineEdit()

        self.tab3.label8 = QLabel("Volume (L) of package:")
        self.tab3.edit8 = QLineEdit()

        self.tab3.edit9 = QCheckBox("Fragile package")

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
        self.tab3.vbox.addWidget(self.tab3.edit9)
        self.tab3.vbox.addWidget(self.tab3.button)
        self.tab3.hbox.addLayout(self.tab3.vbox)
        self.tab3.setLayout(self.tab3.hbox)
        # ---------------------------------

        # Initialize 4th Tab (Info):
        # Contact:
        self.tab4.label0 = QLabel("")
        self.tab4.label1 = QLabel("Phone:")
        self.tab4.label2 = QLabel("+90 XXX XXX XXXX")
        self.tab4.label2.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.tab4.label4 = QLabel("Fax:")
        self.tab4.label5 = QLabel("+90 XXX XXX XXXX")
        self.tab4.label5.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.tab4.label7 = QLabel("E-mail:")
        self.tab4.label8 = QLabel("info@opencargo")
        self.tab4.label8.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.tab4.vbox1 = QVBoxLayout()
        self.tab4.vbox1.addWidget(self.tab4.label1)
        self.tab4.vbox1.addWidget(self.tab4.label2)
        self.tab4.vbox1.addWidget(self.tab4.label0)
        self.tab4.vbox1.addWidget(self.tab4.label4)
        self.tab4.vbox1.addWidget(self.tab4.label5)
        self.tab4.vbox1.addWidget(self.tab4.label0)
        self.tab4.vbox1.addWidget(self.tab4.label7)
        self.tab4.vbox1.addWidget(self.tab4.label8)
        self.tab4.vbox1.addWidget(self.tab4.label0)
        self.tab4.hbox1 = QHBoxLayout()
        self.tab4.hbox1.addLayout(self.tab4.vbox1)
        self.tab4.hbox1.addStretch()
        self.tab4.gr1 = QGroupBox("Contact")
        self.tab4.gr1.setLayout(self.tab4.hbox1)

        # Our Offices:
        self.tab4.label9 = QLabel("Country:")
        self.tab4.edit1 = QLineEdit()
        self.tab4.label10 = QLabel("City:")
        self.tab4.edit2 = QLineEdit()
        self.tab4.label11 = QLabel("District:")
        self.tab4.edit3 = QLineEdit()
        self.tab4.button1 = QPushButton("Search")

        self.tab4.vbox2 = QVBoxLayout()
        self.tab4.vbox2.addWidget(self.tab4.label9)
        self.tab4.vbox2.addWidget(self.tab4.edit1)
        self.tab4.vbox2.addWidget(self.tab4.label10)
        self.tab4.vbox2.addWidget(self.tab4.edit2)
        self.tab4.vbox2.addWidget(self.tab4.label11)
        self.tab4.vbox2.addWidget(self.tab4.edit3)
        self.tab4.vbox2.addWidget(self.tab4.button1)
        self.tab4.hbox2 = QHBoxLayout()
        self.tab4.hbox2.addStretch()
        self.tab4.hbox2.addLayout(self.tab4.vbox2)
        self.tab4.hbox2.addStretch()
        self.tab4.gr2 = QGroupBox("Our Offices")
        self.tab4.gr2.setLayout(self.tab4.hbox2)

        # FAQ
        self.tab4.label12 = QLabel("Select your topic:")
        self.tab4.combo1 = QComboBox()
        self.tab4.button2 = QPushButton("Click for answers")
        self.tab4.vbox3 = QVBoxLayout()
        self.tab4.vbox3.addStretch()
        self.tab4.vbox3.addWidget(self.tab4.label12)
        self.tab4.vbox3.addWidget(self.tab4.combo1)
        self.tab4.vbox3.addWidget(self.tab4.button2)
        self.tab4.vbox3.addStretch()
        self.tab4.hbox3 = QHBoxLayout()
        self.tab4.hbox3.addStretch()
        self.tab4.hbox3.addLayout(self.tab4.vbox3)
        self.tab4.hbox3.addStretch()
        self.tab4.gr3 = QGroupBox("FAQ")
        self.tab4.gr3.setLayout(self.tab4.hbox3)

        # Layout:
        self.tab4.hlayout = QHBoxLayout()
        self.tab4.hlayout.addWidget(self.tab4.gr1)
        self.tab4.hlayout.addWidget(self.tab4.gr3)
        self.tab4.vlayout = QVBoxLayout()
        self.tab4.vlayout.addLayout(self.tab4.hlayout)
        self.tab4.vlayout.addWidget(self.tab4.gr2)

        self.tab4.setLayout(self.tab4.vlayout)

        self.show()
        self.tab3.button.clicked.connect(self.send_data)




    def send_data(self):
        sendername = self.tab3.edit1.text()
        sendernumber = int(self.tab3.edit2.text())
        address = self.tab3.edit3.text()
        recipientName = self.tab3.edit4.text()
        recipientNumber = int(self.tab3.edit5.text())
        deliveryAddress = self.tab3.edit6.text()
        weight = int(self.tab3.edit7.text())
        volume = int(self.tab3.edit8.text())
        sense: str = "non-fragile"
        if self.tab3.edit9.isChecked():
            sense = "fragile"

        self.con = sqlite3.connect("cargo_items.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("Create Table If not exists cargo_items (sendername TEXT,senderNumber INT,address TEXT,recipientName TEXT,recipientNumber INT,deliveryAddress TEXT,Weight INT,Volume INT,sensitive INT)")
        self.cursor.execute("INSERT INTO cargo_items(sendername,senderNumber,address,recipientName,recipientNumber,deliveryAddress,Weight,Volume,sensitive) VALUES(?,?,?,?,?,?,?,?,?)",(sendername,sendernumber,address,recipientName,recipientNumber,deliveryAddress,weight,volume,sense))
        self.con.commit()
        self.succeed()

    def succeed(self):
        self.win = Success()
        self.win.show()


    def staffLogin(self):
        self.win2 = QWidget()
        self.layout2 = QVBoxLayout()
        self.table1 = Table()
        self.load()
    def load(self):
        self.connec = sqlite3.connect('cargo_items.db')
        self.query = "SELECT * FROM cargo_items"
        self.result = self.connec.execute(self.query)
        self.table1.setRowCount(0)

        for row_number,row_data in enumerate(self.result):
            self.table1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table1.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connec.close()
        self.layout2.addWidget(self.table1)
        self.win2.setLayout(self.layout2)
        self.win2.show()


class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.init_table()

    def init_table(self):
        self.setWindowTitle("OpenCARGO Items")
        self.setRowCount(10)
        self.setColumnCount(10)
        self.setFixedHeight(350)
        self.setFixedWidth(1100)
        self.button = QCheckBox(self)
        self.button.setText("Delivered")
        i = 0



app = QApplication(sys.argv)

win1 = Opening()

sys.exit(app.exec_())