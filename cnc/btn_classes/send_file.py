from PyQt4.QtGui import *


class SendFile(QPushButton):
    def __init__(self, parent=None):
        super(SendFile, self).__init__(
            "&Send File", parent)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setWindowTitle("File")
