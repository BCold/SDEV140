'''
Author: Brandon Coldren
Program: The Escape
Last Modified: 12/12/22

This GUI application takes the user on a short adventure; it features multiple outcomes and fail states.

'''

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QFont
import sys

class MainWindow(QMainWindow):
    #Initialize the ROOM_NUM and ROOM_CONTENT class variables
    ROOM_NUM = 0 # Tracks the current "room" number for user throughout the application
    ROOM_CONTENT = () # A list of all values contained within a "room" file. 
    # The list is organized like so: index 0 is the story prompt, indexes 1-3 are user choices, indexes 4-6 are the outcomes, and indexes 7-9 track the "state" of the user after a choice.
    
    def __init__(self):
        '''Constructs the components of the Main Window'''
        super(MainWindow, self).__init__()
        self.ROOM_CONTENT = (self.chooseRoom())
        self.initUI()
        self.center()

    def initUI(self):
        # Construct the MainWindow
        self.setGeometry(0, 0, 1024, 768)
        self.setMaximumSize(1024,768)
        self.setMinimumSize(1024,768)
        self.setWindowTitle("The Escape")

        # Create central widget to act as container for backgroundImage Label
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setStyleSheet("")
        self.setCentralWidget(self.centralwidget)
        
        # Create the backgroundImage label and set it's parameters, as the name implies this label is acting as a background image
        self.backgroundImage = QtWidgets.QLabel(self.centralwidget)
        self.backgroundImage.setGeometry(QtCore.QRect(-4, -8, 1031, 781))
        self.backgroundImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.backgroundImage.setText("")
        self.backgroundImage.setPixmap(QtGui.QPixmap("woodBG.jpg"))
        self.backgroundImage.setScaledContents(True)
        
        # Create a window icon and set it to display
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("keyicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        # Initialize the storyPrompt text box and it's parameters
        self.storyPrompt = QtWidgets.QTextEdit(self, readOnly = True)
        self.storyPrompt.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.storyPrompt.setFont(QFont("Segoe Print", 14))
        self.storyPrompt.move(60,20)
        self.storyPrompt.resize(911, 404)
        self.storyPrompt.setText(self.ROOM_CONTENT[0])

        # Initialize the choice buttons and their parameters
        self.choiceBtn_1 = QtWidgets.QPushButton(self)
        self.choiceBtn_1.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.choiceBtn_1.setFont(QFont("Segoe Print", 14))
        self.choiceBtn_1.setText("1.")
        self.choiceBtn_1.move(72,458)
        self.choiceBtn_1.resize(75,41)

        # Calls the show_Outcome method when clicked
        self.choiceBtn_1.clicked.connect(lambda: self.show_Outcome(0))

        self.choiceBtn_2 = QtWidgets.QPushButton(self)
        self.choiceBtn_2.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.choiceBtn_2.setFont(QFont("Segoe Print", 14))
        self.choiceBtn_2.setText("2.")
        self.choiceBtn_2.move(72, 544)
        self.choiceBtn_2.resize(75,41)
        self.choiceBtn_2.clicked.connect(lambda: self.show_Outcome(1))

        self.choiceBtn_3 = QtWidgets.QPushButton(self)
        self.choiceBtn_3.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.choiceBtn_3.setFont(QFont("Segoe Print", 14))
        self.choiceBtn_3.setText("3.")
        self.choiceBtn_3.move(72,630)
        self.choiceBtn_3.resize(75,41)
        self.choiceBtn_3.clicked.connect(lambda: self.show_Outcome(2))

    # Construct the text boxes that accompany each choice button
        self.choice1_Text = QtWidgets.QTextEdit(self, readOnly = True)
        self.choice1_Text.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.choice1_Text.setFont(QFont("Segoe Print", 14))
        self.choice1_Text.move(152,458)
        self.choice1_Text.resize(808,76)
        self.choice1_Text.setText(self.ROOM_CONTENT[1])

        self.choice2_Text = QtWidgets.QTextEdit(self, readOnly = True)
        self.choice2_Text.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.choice2_Text.setFont(QFont("Segoe Print", 14))
        self.choice2_Text.move(152,544)
        self.choice2_Text.resize(808,76)
        self.choice2_Text.setText(self.ROOM_CONTENT[2])

        self.choice3_Text = QtWidgets.QTextEdit(self, readOnly = True)
        self.choice3_Text.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.choice3_Text.setFont(QFont("Segoe Print", 14))
        self.choice3_Text.move(152,630)
        self.choice3_Text.resize(808,76)
        self.choice3_Text.setText(self.ROOM_CONTENT[3])

    # Construct the quit button
        self.quitBtn = QtWidgets.QPushButton(self)
        self.quitBtn.setStyleSheet("background-color: #faf0e6; border-radius:4px;")
        self.quitBtn.setFont(QFont("Segoe Print", 14))
        self.quitBtn.setText("Quit")
        self.quitBtn.move(437,717)
        self.quitBtn.resize(150, 41)

        # When clicked the quitBtn closes the application
        self.quitBtn.clicked.connect(lambda: sys.exit())

    def center(self):
        '''Centers a PyQt5 window on any display'''
        windowFrame = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(centerPoint)
        self.move(windowFrame.topLeft())
    
    def updateUI(self):
        '''Updates UI elements within the MainWindow'''
        
        # Updates the contents of the ROOM_CONTENT list with text from the pertinent file and then passes the new content to the appropriate widget
        self.ROOM_CONTENT = (self.chooseRoom())
        self.storyPrompt.setText(self.ROOM_CONTENT[0])
        self.choice1_Text.setText(self.ROOM_CONTENT[1])
        self.choice2_Text.setText(self.ROOM_CONTENT[2])
        self.choice3_Text.setText(self.ROOM_CONTENT[3])

    def show_Outcome(self, num = int):
        '''Displays the results of user choices in a pop-up window'''
        
        #Construct the pop-up window and set its parameters
        outcome = QMessageBox()
        outcome.setWindowTitle("Outcome")
        outcome.resize(900,400)
        outcome.setFont(QFont("Segoe Print", 14))
        outcome.setStyleSheet("background-color: #faf0e6;")
        
        # Create a window icon and set it to display
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("keyicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        outcome.setWindowIcon(icon)
        outcome.setStandardButtons(QMessageBox.Ok)
        
        # Evaluates user choices and directs according to the results of said choices. num 0-2 represent the choiceBtn widgets. num 3 & 4 represent fail states.
        if num == 0:
             outcome.setText(self.ROOM_CONTENT[4])
             outcome.buttonClicked.connect(lambda: self.popButton(num))
        
        elif num == 1:
            outcome.setText(self.ROOM_CONTENT[5])
            outcome.buttonClicked.connect(lambda: self.popButton(num))
        
        elif num == 2:
            outcome.setText(self.ROOM_CONTENT[6])
            outcome.buttonClicked.connect(lambda: self.popButton(num))
        
        elif num == 3:
            outcome.setText("You have been captured!\nRestarting. . .")
            self.ROOM_NUM = 0
            outcome.buttonClicked.connect(self.updateUI)
        
        elif num == 4:
             outcome.setText("You have died!\nRestarting. . . ")
             self.ROOM_NUM = 0
             outcome.buttonClicked.connect(self.updateUI)

        elif num == 5:
            outcome.setText("Congratulations, You have escaped!\nThanks for playing!")
            outcome.buttonClicked.connect(lambda: sys.exit())
        outcome.exec_()

    def popButton(self,num):
        '''Evaluates whether the updateUI method should be called or not based upon user choice results'''

        if num == 0 and self.ROOM_CONTENT[7] == "captured\n":
            self.show_Outcome(3)
        
        elif num == 1 and self.ROOM_CONTENT[8] == "captured\n":
            self.show_Outcome(3)
        
        elif num == 2 and self.ROOM_CONTENT[9] == "captured":
            self.show_Outcome(3)
        
        elif num == 0 and self.ROOM_CONTENT[7] == "died\n":
            self.show_Outcome(4)
        
        elif num == 1 and self.ROOM_CONTENT[8] == "died\n":
            self.show_Outcome(4)
        
        elif num == 2 and self.ROOM_CONTENT[9] == "died\n":
            self.show_Outcome(4)

        elif num == 2 and self.ROOM_CONTENT[9] == "win":
            self.show_Outcome(5)
        
        else:
            self.updateUI()

    
    def populateRoom(self, x):
        '''This method populates the ROOM_CONTENT list and returns it to the chooseROOM method'''
        file = open(x, "r")
        room =[]
        
        for line in file:
            room.append(line)
        
        file.close()
        return room
    
    def chooseRoom(self):
        '''This method evaluates the current ROOM_NUM and then assigns the appropriate file to be copied by the populateRoom method. Returns the content to the ROOM_CONTENT list'''
        if self.ROOM_NUM == 0:
            file = "splash.txt"
            content = self.populateRoom(file)
            self.ROOM_NUM += 1
            return content

        elif self.ROOM_NUM == 1:
            file = "room1.txt"
            content = self.populateRoom(file)
            self.ROOM_NUM += 1
            return content
        
        elif self.ROOM_NUM == 2:
            file = "room2.txt"
            content = self.populateRoom(file)
            self.ROOM_NUM += 1
            return content
       
        elif self.ROOM_NUM == 3:
            file = "room3.txt"
            content = self.populateRoom(file)
            self.ROOM_NUM += 1
            return content
        
        elif self.ROOM_NUM == 4:
            file = "room4.txt"
            content = self.populateRoom(file)
            self.ROOM_NUM += 1
            return content
        
        elif self.ROOM_NUM == 5:
            file = "room5.txt"
            content = self.populateRoom(file)
            self.ROOM_NUM += 1
            return content
        
        elif self.ROOM_NUM == 6:
            file = "room6.txt"
            content = self.populateRoom(file)
            return content

# Creates a function to run the application
def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

# runs the application
window()