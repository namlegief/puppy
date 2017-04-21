import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer

# sys.path.insert(1, '..')
from net_ops.pool import get_connections_pool


class ShowClnt(QTableWidget):
    def __init__(self, parent=None):
        super(ShowClnt, self).__init__(parent)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        tableItem = QTableWidgetItem()
        self.setColumnCount(1)
        self.get_agents()

    def get_agents(self):
        curr_agents = get_connections_pool()

        self.setRowCount(len(curr_agents))

        for conn in curr_agents.items():
            self.setItem(0, 0, QTableWidgetItem(conn[0]))

        QTimer.singleShot(3000, self.get_agents)
