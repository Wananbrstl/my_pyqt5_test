#! /home/lbn/miniconda3/envs/pyqt/bin/python
# encoding : utf-8
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class my_label(QLabel):
    def __init__(self, *args, antiliasing=True, **kwargs):
        super(my_label, self).__init__(*args, **kwargs)
        self.Antialiasing = antiliasing
        self.setFixedSize(200, 200)
        self.radius = 100

        # create QPixmap class
        self.target = QPixmap(self.size())
        self.target.fill(Qt.transparent)
        p = QPixmap("Data/Images/head.jpg").scaled(200, 200, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        painter = QPainter(self.target)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.radius, self.radius)
        painter.setClipPath(path)
        painter.drawPixmap(0,0,p)
        self.setPixmap(self.target)
        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
""" 
        painter = QPainter(self.target)
        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        path = QPainterPath()
        path.addRoundedRect(
            -1, 0, self.width(), self.height(), self.radius, self.radius)
        painter.setClipPath(path)
        painter.drawPixmap(-1, 0, p)
        self.setPixmap(self.target)
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = QWidget()
    wind.setWindowTitle("Circle test")
    layout = QHBoxLayout(wind)
    label = my_label()
    layout.addWidget(label)
    wind.show()
    sys.exit(app.exec_())
