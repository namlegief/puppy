import sys
from PyQt4 import QtGui


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.button = QtGui.QPushButton('Test')
        self.edit = QtGui.QTextEdit()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.handleTest)

    def handleTest(self):
        self.edit.append('spam: spam spam spam spam{0}'.format(tst))


if __name__ == '__main__':
    tst = '123'
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
