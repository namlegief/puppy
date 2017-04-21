import sys
import qt_funcs

from PyQt4.QtGui import *

from btn_classes.tcp_server import ServerDlg
from btn_classes.show_clients import ShowClnt
from btn_classes.send_cmds import SendCmds
from btn_classes.send_file import SendFile
from btn_classes.pkg import InstallPkg
from btn_classes.pkg import RemovePkg


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
        mainQWidget = QWidget()
        mainLayout = QFormLayout()
        mainLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)

        label = QLabel('Command:')
        lineEdit = QLineEdit()
        mainLayout.addRow(label, lineEdit)

        ButtonBox = QGroupBox()
        ButtonsLayout = QHBoxLayout()

        # Button_01 = ServerDlg()
        Button_02 = ShowClnt()
        Button_03 = SendCmds()
        Button_04 = SendFile()
        Button_05 = InstallPkg()
        Button_06 = RemovePkg()

        # ButtonsLayout.addWidget(Button_01)
        ButtonsLayout.addWidget(Button_02)
        ButtonsLayout.addWidget(Button_03)
        ButtonsLayout.addWidget(Button_04)
        ButtonsLayout.addWidget(Button_05)
        ButtonsLayout.addWidget(Button_06)

        ButtonBox.setLayout(ButtonsLayout)
        mainLayout.addRow(ButtonBox)

        mainQWidget.setLayout(mainLayout)
        self.setCentralWidget(mainQWidget)
