import sys
import socket

sys.path.insert(1, '../lib')
from config import config

BIND_INTERFACE = config('cnc')['server']['bind_intf']
BIND_PORT = config('cnc')['server']['bind_port']
SIZEOF_UINT32 = 4

connections_pool = {}


def start_server(threadName, log):
    log.info('CNC started in thread {}'.format(threadName))

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind((BIND_INTERFACE, BIND_PORT))
    connection.listen(10)

    i = 0
    while True:
        current_connection, address = connection.accept()
        log.debug('Arrived new connection from: {}'.format(address[0]))
        connections_pool[address[0]] = {i: current_connection}
        i += 1


def clean_pool(threadName, log):
    log.info('pool cleaner started in thread {}'.format(threadName))

    while True:
        # TODO: do clean from aborted connections
        pass


def get_connections_pool():
    return connections_pool
