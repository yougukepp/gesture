#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel

from PyQt5.QtCore import pyqtSignal
from PyQt5.uic import loadUiType, loadUi

from wave_widget import WaveWidget

g_GTWindowUIClass = loadUiType("gt_window.ui")

class GTWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__() 

        # 初始化UI
        self.mUi = g_GTWindowUIClass[0]()
        self.mUi.setupUi(self)

        # 菜单在ui文件中初始化
        # 此处指初始化状态栏
        statusLabel1 = QLabel("状态栏占位标签")
        self.mStatusBar = self.mUi.statusbar
        self.mStatusBar.addWidget(statusLabel1) 

        # 核心widget wave_widget
        self.mWaveWidget = WaveWidget()
        self.setCentralWidget(self.mWaveWidget)
        
        # 标题
        self.setWindowTitle("手势控制上位机")

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    win = GTWindow()
    win.show()
    sys.exit(app.exec_())

