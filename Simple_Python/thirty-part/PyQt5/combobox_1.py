__author__ = 'tim'

from PyQt5.QtWidgets import QApplication,QComboBox
import sys

app=QApplication(sys.argv)
combobox=QComboBox()
combobox.addItems(['Large','medium','Small'])
combobox.show()
sys.exit(app.exec_())
