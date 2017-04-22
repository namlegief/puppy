from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SendCmds(QPushButton):
    def __init__(self, parent=None):
        super(SendCmds, self).__init__(
            "&Send Commands", parent)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setWindowTitle("Commands")
