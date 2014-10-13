#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.resize(250,150)
        self.setWindowTitle('MenuBar')
        exit=QAction(QIcon('48.png'),'Exit',self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        exit.triggered.connect(qApp.exit)

        self.statusBar()
        menubar=self.menuBar()
        file=menubar.addMenu('&File')
        file.addAction(exit)

app=QApplication(sys.argv)
main=MainWindow()
main.show()
sys.exit(app.exec_())
