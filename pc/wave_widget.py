#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPalette

class WaveWidget(QWidget):
    def __init__(self, parent=None):
        super(WaveWidget, self).__init__(parent) 
        
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.black) 
        self.setPalette(palette);

        # 拖拽起点
        self.mDragStart = None 
        
    def paintEvent(self, paintEvent):
        painter = QPainter(self) 

    # 交互类函数
    def mousePressEvent(self, mouseEvent):
        pos = mouseEvent.pos()
        self.mDragStart = pos
        print("开始拖拽:(%d,%d)" % (pos.x(), pos.y()))

    def mouseReleaseEvent (self, mouseEvent):
        pos = mouseEvent.pos()
        x = pos.x() - self.mDragStart.x()
        y = pos.y() - self.mDragStart.y()

        if 0 == x and 0 == y:
            print('没有拖拽')
            return

        if 0 != x: 
            print('左右移动:%d' % x) 

        if 0 != y:
            print('上下移动:%d' % y)

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    win = WaveWidget()
    win.show()
    sys.exit(app.exec_())

