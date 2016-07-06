#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QLabel

from point import GTPoint

class StatusBar(QStatusBar):
    def __init__(self, parent=None):
        QStatusBar.__init__(self, parent)

        self.mLabelPhyPos = QLabel("物理坐标:(nan,nan)")
        self.mLabelPaintPos = QLabel("绘制坐标:(nan,nan)")
        self.addWidget(self.mLabelPhyPos)
        self.addWidget(self.mLabelPaintPos)

    def Move(self, pos, height):
        gtPoint = GTPoint(pos, height)
        paintLabelText = "绘制坐标:" + "%d,%d" % (gtPoint.X(), gtPoint.Y())
        self.mLabelPaintPos.setText(paintLabelText)

        phyLabelText = "物理坐标:" + "%d,%d" % (0,0)
        self.mLabelPhyPos.setText(phyLabelText)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = StatusBar()
    win.show()

    sys.exit(app.exec_())
