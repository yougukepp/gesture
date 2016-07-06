#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WaveWidget(QWidget):
    #msMove = pyqtSignal(QPoint, name='msMove')
    msMove = pyqtSignal(['QPoint', 'int'], name = "msMove")

    def __init__(self, parent=None):
        super(WaveWidget, self).__init__(parent) 
        
        self.setMouseTracking(True) # 鼠标跟踪
        self.setCursor(Qt.BlankCursor) # 隐藏鼠标
        self.mPos = None # 鼠标当前点

    def paintEvent(self, paintEvent):
        painter = QPainter(self) 

        # 清屏
        painter.fillRect(0, 0, self.width(), self.height(), Qt.black)
        # 绘制坐标系
        self.drawAxes(painter)
        # 绘制鼠标位置十字线
        self.drawMouseCross(painter)

        painter.end() 

    def drawAxes(self, painter): 
        metrics = painter.fontMetrics() 
        
        textHeight = metrics.ascent() + metrics.descent() 
        leftWidth = metrics.width("V")
        rightWidth = metrics.width("ms") 
        width = leftWidth * 3
        height = self.height() - textHeight  * 2

        # 画坐标系
        pen = QPen(Qt.red)
        pen.setWidth(1)
        painter.setPen(pen)
        step = 50 # 间距50像素一个
        lineLength = 5 # 线长
        # 坐标原点
        painter.drawText(width, height + lineLength * 3, "O");
        # 画横坐标 
        painter.drawLine(width, height, self.width() - 10, height); 
        # 横坐标的标志点
        length = self.width() - width - 10
        shortLineNums = int(length / step)
        #print(length)
        #print(shortLineNums)
        for i in range(0, shortLineNums):
            x1 = (i + 1) * step 
            x2 = x1
            y1 = height
            y2 = height + lineLength
            painter.drawLine(x1, y1, x2, y2 )
            text = "%d" % (i+1)
            painter.drawText(x2 + 2, y2 + lineLength * 2, text)

        # 画纵坐标 
        painter.drawLine(width, height, width, 10); 
        length = height - 10
        shortLineNums = int(length / step)
        #print(length)
        #print(shortLineNums)
        for i in range(0, shortLineNums):
            x1 = width - lineLength
            x2 = width
            y1 = self.height() - ((i + 1) * step)
            y2 = y1
            painter.drawLine(x1, y1, x2, y2 )
            text = "%d" % (i+1)
            painter.drawText(x2 - lineLength * 3 , y2 + 10, text)

    def drawMouseCross(self, painter): 
        if None != self.mPos:
            x = self.mPos.x()
            y = self.mPos.y() 
            pen = QPen(Qt.gray)
            pen.setWidth(1)
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
            painter.drawLine(x, 0, x, self.height())
            painter.drawLine(0, y, self.width(), y)

    # 交互类函数
    def mousePressEvent(self, mouseEvent):
        pass

    def mouseReleaseEvent (self, mouseEvent):
        pass

    def mouseMoveEvent(self, event):
        p = QPoint(event.pos())
        self.mPos = p
        self.msMove.emit(p , self.height())
        self.update()

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    win = WaveWidget()
    win.show()
    sys.exit(app.exec_())

