#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QLabel

class StatusBar(QStatusBar):
    def __init__(self, parent=None):
        QStatusBar.__init__(self, parent)

        self.mLabelPaintPos = QLabel("绘制坐标:(nan,nan)")
        self.mLabelPhyPos = QLabel("物理坐标:(nan,nan)")
        self.addWidget(self.mLabelPaintPos)
        self.addWidget(self.mLabelPhyPos)

    def Move(self, pos):
        labelText = "当前位置:"
        self.mLabelPaintPos.setText(labelText)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = StatusBar()
    win.show()

    sys.exit(app.exec_())
