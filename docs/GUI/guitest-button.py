import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.type_area = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("Clear")
        self.print_text = QtWidgets.QPushButton("Print")
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.type_area)
        vbox.addWidget(self.clear)
        vbox.addWidget(self.print_text)
        vbox.addStretch()
        self.setLayout(vbox)
        
        self.clear.clicked.connect(self.click)
        self.print_text.clicked.connect(self.click)
        
        self.show()

    def click(self):
        sender = self.sender()
        
        if(sender.text() == "Clear"):
            self.type_area.clear()
        else:
            win2 = Window()
            

# MAIN:
app = QtWidgets.QApplication(sys.argv)

win1 = Window()

sys.exit(app.exec_())