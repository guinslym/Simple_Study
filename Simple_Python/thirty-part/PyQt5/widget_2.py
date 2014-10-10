#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
import sys

class Icon(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('48.png'))

app=QApplication(sys.argv)
icon=Icon()
icon.show()
sys.exit(app.exec_())