# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/4 22:37
# 文件名：BookShopSystem.py
# 开发工具：

import LoginUI
from user_window import User_MainWindow
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Login()
    mainWindow.ui.show()
    sys.exit(app.exec_())