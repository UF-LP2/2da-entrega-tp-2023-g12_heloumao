import sys
from PyQt6.QtGui import*
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel
app=QApplication(sys.argv)
app.exec()
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("My App")
        label=QLabel("This is awesome")
        self.setCentralWidget(label)
        window=MainWindow()
        window.show()