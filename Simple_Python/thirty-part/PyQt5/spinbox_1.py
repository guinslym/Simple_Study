__author__ = 'tim'

from PyQt5.QtWidgets import QApplication,QSpinBox
import sys

app=QApplication(sys.argv)
spinbox=QSpinBox()                        #实例化1个Spinbox对象
spinbox.setRange(18,60)                   #设置取值范围
spinbox.setSingleStep(2)                  #设置步长
spinbox.setMaximumHeight(100)             #设置最大高度
spinbox.setMaximumWidth(200)              #设置最大宽度
spinbox.setMinimumWidth(100)
spinbox.setMinimumHeight(20)
spinbox.show()
sys.exit(app.exec_())
