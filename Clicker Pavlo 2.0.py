from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 
import os

os.system("mode con cols=25 lines=4")
global top
top = 10

class Pavlo(QMainWindow):

    def __init__(self):
        super(Pavlo,self).__init__()


        self.setWindowTitle("Pavlo")
        self.setGeometry(0,0,500,500)

        self.text1 = QtWidgets.QLabel(self)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Add match")
        self.button.adjustSize()
        self.button.clicked.connect(self.addMatch)
        print(top)

        


    def addMatch(self):
        self.text1.setText("hello")
        self.text1.move(top,40)
        self.text1.adjustSize()
        

 
        



def Clicker():
    app = QApplication(sys.argv)
    window = Pavlo()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Clicker()
