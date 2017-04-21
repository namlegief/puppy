from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer
from net_ops.pool import get_connections_pool

connections_map = {}

class ShowClnt(QTableWidget):
    def __init__(self, parent=None):
        super(ShowClnt, self).__init__(parent)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.cellActivated.connect(self.handleCellActivated)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        tableItem = QTableWidgetItem()
        self.setColumnCount(1)
        self.get_agents()

    def get_agents(self):
        curr_agents = get_connections_pool()

        self.setRowCount(len(curr_agents))

        i = 0
        for conn in curr_agents.items():
            self.setItem(i, 0, QTableWidgetItem(conn[0]))
            connections_map[i] = conn[0]
            i += 1

        QTimer.singleShot(3000, self.get_agents)

    def handleCellActivated(self, row, column):
        print row, column
