import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

sys.path.insert(1, '../lib')

from config import config

BIND_INTERFACE = config('cnc')['server']['bind_intf']
BIND_PORT = config('cnc')['server']['bind_port']
SIZEOF_UINT32 = 4


class ServerDlg(QPushButton):
    def __init__(self, parent=None):
        super(ServerDlg, self).__init__(
            "&Stop Server", parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.tcpServer = QTcpServer(self)
        self.tcpServer.listen(QHostAddress(BIND_INTERFACE), BIND_PORT)
        self.connect(self.tcpServer, SIGNAL("newConnection()"),
                     self.addConnection)
        self.connections = []

        self.connect(self, SIGNAL("clicked()"), self.close)
        font = self.font()
        font.setPointSize(24)
        self.setFont(font)
        self.setWindowTitle("Server")

    def addConnection(self):
        clientConnection = self.tcpServer.nextPendingConnection()
        clientConnection.nextBlockSize = 0
        self.connections.append(clientConnection)

        self.connect(clientConnection, SIGNAL("readyRead()"),
                     self.receiveMessage)
        self.connect(clientConnection, SIGNAL("disconnected()"),
                     self.removeConnection)
        self.connect(clientConnection, SIGNAL("error()"),
                     self.socketError)

    def receiveMessage(self):
        for s in self.connections:
            if s.bytesAvailable() > 0:
                stream = QDataStream(s)
                stream.setVersion(QDataStream.Qt_4_2)

                if s.nextBlockSize == 0:
                    if s.bytesAvailable() < SIZEOF_UINT32:
                        return
                    s.nextBlockSize = stream.readUInt32()
                if s.bytesAvailable() < s.nextBlockSize:
                    return

                textFromClient = stream.readQString()
                s.nextBlockSize = 0
                self.sendMessage(textFromClient,
                                 s.socketDescriptor())
                s.nextBlockSize = 0

    def sendMessage(self, text, socketId):
        for s in self.connections:
            if s.socketDescriptor() == socketId:
                message = "You> {}".format(text)
            else:
                message = "{}> {}".format(socketId, text)
            reply = QByteArray()
            stream = QDataStream(reply, QIODevice.WriteOnly)
            stream.setVersion(QDataStream.Qt_4_2)
            stream.writeUInt32(0)
            stream.writeQString(message)
            stream.device().seek(0)
            stream.writeUInt32(reply.size() - SIZEOF_UINT32)
            s.write(reply)

    def removeConnection(self):
        pass

    def socketError(self):
        pass
