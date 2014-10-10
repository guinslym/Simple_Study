#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox

class MessageBox(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('message box')

    def closeEvent(self, QCloseEvent):
        reply=QMessageBox.question(self,'Message','Are you sure to quit',QMessageBox.Yes,QMessageBox.No)

        if reply==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app=QApplication(sys.argv)
mb=MessageBox()
mb.show()
sys.exit(app.exec_())
