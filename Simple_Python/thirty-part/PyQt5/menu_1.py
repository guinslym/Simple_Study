#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'tim'

from PyQt5.QtWidgets import QApplication,QMenuBar
import sys

app=QApplication(sys.argv)
menubar=QMenuBar()                           #QMenubar是横向菜单栏
files=menubar.addMenu('File')                #添加菜单
menubar.addMenu('Edit')
menubar.addMenu('View')
menubar.addMenu('Code')
menubar.addMenu('Run')
menubar.addMenu('Tools')
files.addAction('Open')                     #添加菜单下子菜单
project=files.addAction('New Project')
Exit=files.addAction('Exit')
files.addActions([project,Exit])            ##添加1组子菜单
menubar.show()
sys.exit(app.exec_())