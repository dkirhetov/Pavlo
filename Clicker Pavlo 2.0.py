from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 
import os

top = 30


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
        self.text1 = QtWidgets.QMessageBox(self)
        self.text1.setText("Andrey, smotri how it delaetsa")
        self.text1.move(10,top)
        self.text1.adjustSize()
        self.text1.exec()
        top +=10

 
        


 
def Clicker():

    app = QApplication(sys.argv)
    window = Pavlo()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    Clicker()
