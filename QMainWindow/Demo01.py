#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
QMainWindow包括四个部分：
    1. Menu Bar ： 位于MainWindow最上面
    2. ToolBars :  位于Center Widget外层
    3. Center Widget： 只有一个，位于最中间
    4. status bar ：位于最下方，通常显示一些状态信息
""" 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWind(QMainWindow):
    def __init__(self):
        super(MainWind, self).__init__()
        self.setWindowTitle("title")
        self.setGeometry(500,500,500,500)
        self.create_btn = QPushButton("CREATE")
        # self.addToolBa的的.create_btn)
        self.status_bar = QStatusBar(parent=self)
        self.status_bar.showMessage("this is a status bar", 5000)
        self.status_label = QLabel("Status Label")
        self.status_bar.addWidget(self.status_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWind()
    main.show()

    sys.exit(app.exec_())
