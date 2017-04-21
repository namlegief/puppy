import sys
import main_window

sys.path.insert(1, '../lib')

from config import config


def create_main_window():
    w = main_window.mainWindow()

    w.resize(config('cnc')['window']['height'],
             config('cnc')['window']['width'])
    w.setWindowTitle("CNC Server")

    return w
