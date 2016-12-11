from cnc import network
from cnc import time
import tools

config = tools.parse_config()

clock = time.get_current_time()
segment = network.find_segment(config['cnc_if_name'])
gateway = network.get_default_ipv4_gw()
dns_server = network.get_dns_server()

def print_header(clock ,segment, dns_server,gateway ):
    print ("################################################################################")
    print ("  Python 102          Name: Alex & Jenia                  Time: {0} ".format (clock))
    print ("################################################################################")
    print (" Segment:{0}\n DNS:{1} \n Gateway:{2}\n " .format (segment, dns_server, gateway))
    print ("################################################")
    print ("""              Menu
              ----
      """)


def display_main_menu():
    print_header(clock, segment, dns_server, gateway)
    menu = {
        '1': 'Show all clients',
        '2': 'Send commands to all client',
        '3': 'Transfer file to clients all clients',
        '4': 'Install something on all clients',
        '5': 'Remove something from all clients',
    }
    for key, value in menu.iteritems():
        print(key, '.', value)


def display_sub_menu():
    pass


def dislay_menu(menu_level):
    if menu_level == 'main':
        display_main_menu()
    if menu_level == 'sub':
        display_sub_menu()