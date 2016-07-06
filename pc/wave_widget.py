#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WaveWidget(QWidget):
    def __init__(self, parent=None):
        super(WaveWidget, self).__init__(parent) 

        # 鼠标跟踪
        self.setMouseTracking(True)
        self.setMargin(5)

        # 拖拽起点
        self.mDragStart = None 
        
    def paintEvent(self, paintEvent):
        painter = QPainter(self) 

        # 清屏
        painter.fillRect(0, 0, self.width(), self.height(), Qt.black)
        self.drawAxes(painter)

        painter.end() 

    def drawAxes(self, painter): 
        metrics = painter.fontMetrics() 
        
        textHeight = metrics.ascent() + metrics.descent() 
        leftWidth = metrics.width("V")
        rightWidth = metrics.width("ms") 
        width = leftWidth * 3
        height = self.height() - textHeight  * 2
        
        """
        # 绘制外框 
        pen = QPen(Qt.blue)
        pen.setWidth(10)
        painter.setPen(pen)
        painter.drawRect(0, 0, self.width() -1, self.height() - 1)
        """

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

        """
        for (int i = 1; i <= 12; ++i) 
        { 
            QString month = tr("%1月").arg(i); 
            int stringWidth = metrics.width(month); 
            
            # 绘制坐标刻度 
            painter.drawLine(deltaX * i, 0, deltaX * i, 4); 
            # 绘制坐标处的月 
            int monthX = deltaX * (i - 1) + ((deltaX - stringWidth) / 2); 
            painter.drawText(monthX, textHeight, month); 
        } 
        
        # 画纵坐标 
        painter.drawLine(0, 0, 0, -height); 
        painter.drawText(-metrics.width(tr("(件)")), 
                        -(deltaY * count + textHeight / 2 + metrics.descent()), 
                        tr("(件)")); 
                        
        for (int i = 1; i <= count; ++i) 
        { 
            QString value = QString("%1").arg(i * totalCount / count); 
            int stringWidth = metrics.width(value); 
            
            # 绘制坐标刻度 
            painter.drawLine(-4, -i * deltaY, 0, -i * deltaY); 
            # 绘制坐标值 
            # painter.drawText(-stringWidth - 4, -i * deltaY + stringHeight / 2, value); 
            painter.drawText(-stringWidth - 4, -(deltaY * i + textHeight / 2 - metrics.ascent()), value); 
        }
        """

    def setMargin(self, margin):
        self.mMargin = margin

    def getMargin(self):
        return self.mMargin

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

