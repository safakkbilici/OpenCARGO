import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.text_area = QtWidgets.QLabel("Bana henüz tıklanmadı.")
        self.button = QtWidgets.QPushButton("Bana tıkla")
        self.count = 0
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.text_area)
        vbox.addWidget(self.button)
        vbox.addStretch()
           
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addStretch()
        
        self.setLayout(hbox)
        
        self.button.clicked.connect(self.click)
        
        self.show()
        
    def click(self):
        self.count = self.count + 1
        self.text_area.setText("Bana " + str(self.count) + " kere tıklandı.")
        
app = QtWidgets.QApplication(sys.argv)

pencere = Window()

sys.exit(app.exec_())

