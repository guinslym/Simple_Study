__author__ = 'tim'


from PyQt5.QtWidgets import QApplication,QTabBar
import sys

app=QApplication(sys.argv)
TabBar=QTabBar()
TabBar.addTab('Food')
TabBar.addTab('Drink')
TabBar.show()
sys.exit(app.exec_())