import sys

from threading import Thread
from net_ops import pool
from main_window import start_gui

sys.path.insert(1, '../lib')

from log import setup_logger

log = setup_logger('cnc')

if __name__ == '__main__':

    try:
        log.info('Starting CNC server')
        cnc_worker = Thread(target=pool.start_server, args=("Pooler", log))
        cnc_worker.start()

        log.info('Starting GUI interface')
        gui_worker = Thread(target=start_gui, args=("GUI", log))
        gui_worker.start()

        log.info('Starting pool cleaner')
        cleaner_worker = Thread(target=pool.clean_pool, args=("cleaner", log))
        cleaner_worker.start()

    except KeyboardInterrupt:
        pass
