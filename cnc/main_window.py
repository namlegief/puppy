import sys
import qt_funcs

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from btn_classes.tcp_server import ServerDlg
from btn_classes.show_clients import ShowClnt
from btn_classes.send_cmds import SendCmds
from btn_classes.send_file import SendFile
from btn_classes.pkg import InstallPkg
from btn_classes.pkg import RemovePkg

from net_ops.send_cmd import execute, install, remove


def start_gui(threadName, log):
    log.debug('GUI has been started in thread {}'.format(threadName))
    app = QApplication(sys.argv)

    main_window = qt_funcs.create_main_window()
    app.setActiveWindow(main_window)
    main_window.show()
    app.exec_()


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # http://doc.qt.io/qt-4.8/layout.html
        self.mainQWidget = QWidget()
        self.mainLayout = QFormLayout()
        self.mainLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)

        self.label = QLabel('Command:')
        self.lineEdit = QLineEdit()
        self.mainLayout.addRow(self.label, self.lineEdit)

        self.ButtonBox = QGroupBox()
        self.ButtonsLayout = QHBoxLayout()

        # Button_01 = ServerDlg()
        self.Button_02 = ShowClnt()
        self.Button_03 = SendCmds()
        self.Button_04 = SendFile()
        self.Button_05 = InstallPkg()
        self.Button_06 = RemovePkg()

        # ButtonsLayout.addWidget(Button_01)
        self.ButtonsLayout.addWidget(self.Button_02)
        self.ButtonsLayout.addWidget(self.Button_03)
        self.ButtonsLayout.addWidget(self.Button_04)
        self.ButtonsLayout.addWidget(self.Button_05)
        self.ButtonsLayout.addWidget(self.Button_06)

        self.ButtonBox.setLayout(self.ButtonsLayout)
        self.mainLayout.addRow(self.ButtonBox)

        self.mainQWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainQWidget)

        self.connect(self.Button_03, SIGNAL("clicked()"), self.send_commands)
        self.connect(self.Button_05, SIGNAL("clicked()"), self.install_pkg)
        self.connect(self.Button_06, SIGNAL("clicked()"), self.remove_pkg)

    def send_commands(self):
        execute(self.Button_02.getSelectedAgents(), self.lineEdit.text())

    def install_pkg(self):
        install(self.Button_02.getSelectedAgents(), self.lineEdit.text())

    def remove_pkg(self):
        remove(self.Button_02.getSelectedAgents(), self.lineEdit.text())
