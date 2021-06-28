from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 
import os

os.system("mode con cols=25 lines=4")


class Pavlo(QMainWindow):
    def __init__(self):
        super(Pavlo,self).__init__()

        self.setWindowTitle("Pavlo")
        self.setGeometry(0,0,500,500)

        self.text = QtWidgets.QLabel(self)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Add match")
        self.button.adjustSize()

        self.button.clicked.connect(self.addMatch)

        


    def addMatch(self):
        self.text.setText("hello")
        self.text.move(10,40)
        self.text.adjustSize()
        
        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setText("del")
        self.cancelButton.move(50,40)
        self.cancelButton.adjustSize()

       



def Clicker():
    app = QApplication(sys.argv)
    window = Pavlo()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Clicker()
