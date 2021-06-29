from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys 
import os
import random

top = 30
Id = 0
matchId = 0
matches = []
m = False

os.system("mode con cols=25 lines=4")                    #settings of console

class Pavlo(QMainWindow):

    def __init__(self):
        super(Pavlo,self).__init__()

        self.setWindowTitle("Pavlo")
        self.setGeometry(80,38,280,250)                 #initializing the window
        self.setWindowIcon(QIcon('icon.png'))           #adding icon

        self.buttonT = QtWidgets.QPushButton(self)       #adding button
        self.buttonT.setText("Total")
        self.buttonT.adjustSize()
        self.buttonT.clicked.connect(self.showButton)

        self.buttonIT = QtWidgets.QPushButton(self)       #adding button
        self.buttonIT.setText("Ind. total")
        self.buttonIT.adjustSize()
        self.buttonIT.move(100,0)
        self.buttonIT.clicked.connect(self.showButton)
        self.buttonIT.clicked.connect(self.numIT)

    def numIT(self):
        global m
        m = True  
                   

    def showButton(self):

        self.buttonT.deleteLater()

        self.buttonIT.deleteLater()

        self.button = QtWidgets.QPushButton(self)       #adding button
        self.button.setText("Add match")
        self.button.adjustSize()
        self.button.clicked.connect(self.addMatch)      #button reacting
        self.button.show()

    def addMatch(self):                                 #button reaction
        global m
        global top
        global Id
        global matchId
        global matches
        matches.append([str(random.randint(0, 250)),str(random.randint(0, 250)),str(random.randint(0, 250))])

        self.text = QtWidgets.QLabel(self)
        self.text.setText("Match "+str(matchId+1))
        self.text.move(10,top+5)
        self.text.adjustSize()
        self.text.show()

        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setText("Del")
        self.cancelButton.move(60,top)
        self.cancelButton.adjustSize()
        self.cancelButton.setStyleSheet('background: rgb('+matches[Id][0]+','+matches[Id][1]+','+matches[Id][2]+');')
        self.cancelButton.show()
        self.cancelButton.clicked.connect(self.deleteMutch)

        #self.reloadButton = QtWidgets.QPushButton(self)
        #self.reloadButton.setText("Reload")
        #self.reloadButton.move(140,top)
        #self.reloadButton.adjustSize()
        #self.reloadButton.setStyleSheet('background: rgb('+matches[Id][0]+','+matches[Id][1]+','+matches[Id][2]+');')
        #self.reloadButton.show()
        #self.reloadButton.clicked.connect(self.reloadRegion)

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setText("Press W!")
        self.text1.move(220,top+5)
        self.text1.adjustSize()
        self.text1.show()

        if m and (Id % 2 == 0 or Id == 0):
            matchId = matchId
        else:
            matchId +=1

        Id += 1
        top += 20

    def deleteMutch(self):
        self.text.deleteLater()
        self.cancelButton.deleteLater()
        self.text1.deleteLater()
         
    # def reloadRegion(self):
        #code 4 reloading Pavlo

        #below some shit is happening
        #only Andrey knows it

   
def Clicker():

    app = QApplication(sys.argv)
    window = Pavlo()
    window.show()
    sys.exit(app.exec_())                               #event loop

if __name__ == "__main__":                              #if main file is run
    Clicker()                                           #start clicker
