from PyQt4.QtGui import *


class InstallPkg(QPushButton):
    def __init__(self, parent=None):
        super(InstallPkg, self).__init__(
            "&Install package", parent)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setWindowTitle("Install Package")


class RemovePkg(QPushButton):
    def __init__(self, parent=None):
        super(RemovePkg, self).__init__(
            "&Remove package", parent)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setWindowTitle("Remove Package")
