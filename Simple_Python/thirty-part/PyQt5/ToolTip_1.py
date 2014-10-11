#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QWidget, QToolTip
from PyQt5.QtGui import QFont

class Tooptip(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Tooltip')
        self.setToolTip('This is a <b> QWidget </b>widget')
        QToolTip.setFont(QFont('oldEnglish',10))

app=QApplication(sys.argv)
tooltip=Tooptip()
tooltip.show()
sys.exit(app.exec_())

