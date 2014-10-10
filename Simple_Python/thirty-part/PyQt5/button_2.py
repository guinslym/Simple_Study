#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,qApp
from PyQt5.QtCore import pyqtSignal,pyqtSlot

class QuitButton(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QuitButton')

        quit=QPushButton('close',self)
        quit.setGeometry(10,10,60,35)

        #QObject.connect(quit,pyqtSignal('click'),qApp,pyqtSlot('quit'))

app=QApplication(sys.argv)
qb=QuitButton()
qb.show()
sys.exit(app.exec_())
