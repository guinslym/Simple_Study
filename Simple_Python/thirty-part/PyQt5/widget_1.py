#!/usr/bin/env/python
#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication,QWidget
import sys

app=QApplication(sys.argv)                       #Application对象
widget=QWidget()                                 #用户界面类父类
widget.resize(250,150)                           #改变窗口部件的大小
widget.setWindowTitle('simple')                  #设置窗口部件的标题
widget.show()
sys.exit(app.exec_())