from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer, QString
from net_ops.pool import get_connections_pool

connections_map = {}


class ShowClnt(QTableWidget):
    def __init__(self, parent=None):
        super(ShowClnt, self).__init__(parent)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setColumnCount(1)
        self.get_agents()
        self.setHorizontalHeaderLabels(str(QString("Agent IP")))
        self.setSelectionMode(QAbstractItemView.MultiSelection)

        self.cellClicked.connect(self.showIndex)


    def get_agents(self):
        curr_agents = get_connections_pool()

        self.setRowCount(len(curr_agents))

        i = 0
        for conn in curr_agents.items():
            self.setItem(i, 0, QTableWidgetItem(conn[0]))
            connections_map[i] = conn[0]
            i += 1

        QTimer.singleShot(3000, self.get_agents)

    def showIndex(self, row, column):

        a = self.selectedIndexes()
        for address in a:
            print connections_map[address.row()]
        pass
