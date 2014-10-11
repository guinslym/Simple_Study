#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication, QLabel,QWidget,QVBoxLayout


class VBox(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle('VBox')
        self.resize(250,150)
        main=QVBoxLayout()
        label1=QLabel('One')
        label2=QLabel('Two')
        main.addWidget(label1)
        main.addWidget(label2)
        self.setLayout(main)

app = QApplication(sys.argv)
box = VBox()
box.show()
sys.exit(app.exec_())