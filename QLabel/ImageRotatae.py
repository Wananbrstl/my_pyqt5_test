#! /usr/bin/env python
# encoding : utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class my_label(QLabel):
    def __init__(self):
        super(my_label, self).__init__()
        self.resize(800, 600)
        self.layout = QHBoxLayout(self)

        self.layout.addWidget(QLabel(self, pixmap=QPixmap("Data/head.jpg")))
        # self.gif = QMovie("Data/loading.gif")
        self.gif = QPixmap("Date/bg1.jpg")
        gif_label = QLabel(self)
        gif_label.setPixmap(self.gif)
        self.layout.addWidget(gif_label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = QWidget()
    wind.setFixedSize(800,600)
    layout = QHBoxLayout(wind)
    layout.addWidget(my_label())
    wind.show()
    sys.exit(app.exec_())
