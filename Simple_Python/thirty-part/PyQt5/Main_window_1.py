#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)

        self.resize(250,150)
        self.setWindowTitle('StatusBar')
        self.statusBar().showMessage('Ready')

app=QApplication(sys.argv)
main=MainWindow()
main.show()
sys.exit(app.exec_())
