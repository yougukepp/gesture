#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QPoint

# 内部格式 表示数据点
# GTPoint左下为原点
# QPoint左上为原点
class GTPoint():
    def __init__(self, qPoint, height):
        self.mQPoint = qPoint
        self.mX = self.mQPoint.x()
        self.mY = height - self.mQPoint.y()
        if self.mY < 0:
            print("GTPoint初始化,参数错误")
            exit(0)

    def X(self):
        return self.mX

    def Y(self):
        return  self.mY

    def GetStr(self):
        pos =  "(%d, %d)" % (self.mX, self.mY)
        return pos

    def GetQPoint(self):
        return self.mQPoint

    def Print(self):
        print("(%3d,%3d)" % (self.X(), self.Y()), end = "")

if __name__ == "__main__":
    gtPoint = GTPoint(QPoint(10, 10), 100)
    if 10 == gtPoint.X() and 90 == gtPoint.Y() :
        print("测试通过")
    else:
        print("测试失败")



