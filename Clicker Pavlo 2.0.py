from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 
import os

top = 30
Id = 1


os.system("mode con cols=25 lines=4")


class Pavlo(QMainWindow):

    def __init__(self):
        super(Pavlo,self).__init__()

        self.setWindowTitle("Pavlo")
        self.setGeometry(80,38,500,500)

        

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Add match")
        self.button.adjustSize()
        self.button.clicked.connect(self.addMatch)

    def addMatch(self):
        global top
        global Id
        self.text = QtWidgets.QLabel(self)
        self.text.setText("Match "+str(Id))
        self.text.move(10,top+5)
        self.text.adjustSize()
        self.text.show()
        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setText("Del")
        self.cancelButton.move(60,top)
        self.cancelButton.adjustSize()
        self.cancelButton.show()
        Id += 1
        top += 20

 
        


 
def Clicker():

    app = QApplication(sys.argv)
    window = Pavlo()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    Clicker()
