#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from gt_window import GTWindow

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    win = GTWindow()
    win.move(0,0)
    win.show()
    sys.exit(app.exec_())

