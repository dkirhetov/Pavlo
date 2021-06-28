from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 
import os

top = 30                                         #starting coordinates of labels/buttons


os.system("mode con cols=25 lines=4")            #Andrey, add something, I don't know what is it


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
    sys.exit(app.exec_())

if __name__ == "__main__":
    Clicker()
