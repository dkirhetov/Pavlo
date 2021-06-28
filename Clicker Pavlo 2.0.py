from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 
import os

top = 30
Id = 1


os.system("mode con cols=25 lines=4")            #settings of console


class Pavlo(QMainWindow):

    def __init__(self):
        super(Pavlo,self).__init__()

        self.setWindowTitle("Pavlo")
        self.setGeometry(80,38,500,500)         #initializing the window

        

        self.button = QtWidgets.QPushButton(self)       #adding button
        self.button.setText("Add match")
        self.button.adjustSize()
        self.button.clicked.connect(self.addMatch)      #button reacting

    def addMatch(self):                                 #button reaction
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
        self.cancelButton.clicked.connect(self.deleteMutch)
        Id += 1
        top += 20

    def deleteMutch(self):
        self.text.deleteLater()
        

        self.text1 = QtWidgets.QLabel(self)             #creating text field
        self.text1.setText("hello")
        self.text1.move(10,top)
        self.text1.adjustSize()
        self.text1.show()                               #make it visible
        top += 20                                       #move starter coordinates down

 
        
        #below some shit is happening
        #only Andrey knows it

 
def Clicker():

    app = QApplication(sys.argv)
    window = Pavlo()
    window.show()
    sys.exit(app.exec_())                               #event loop

if __name__ == "__main__":                              #if main file is run
    Clicker()                                           #start clicker
