#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QSlider,QSpinBox,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt

class Slide(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle('Slide')
        self.resize(250,100)
        main=QVBoxLayout()
        label=QLabel('0')
        slider=QSlider(Qt.Horizontal)
        spinbox=QSpinBox()
        main.addWidget(label)
        main.addWidget(spinbox)
        main.addWidget(slider)
        spinbox.valueChanged.connect(label.setNum)
        spinbox.valueChanged.connect(slider.setValue)
        slider.valueChanged.connect(label.setNum)
        slider.valueChanged.connect(spinbox.setValue)
        self.setLayout(main)


app=QApplication(sys.argv)
s=Slide()
s.show()
sys.exit(app.exec_())
