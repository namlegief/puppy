import tools

from cnc import network
from cnc import time
from tasks import agents_list

config = tools.get_bind_settings()


def print_header():

    clock = time.get_current_time()
    segment = network.find_segment(config['cnc_if_name'])
    gateway = network.get_default_ipv4_gw()
    dns_server = network.get_dns_server()

    print ("################################################################################")
    print ("  Python 102          Name: Alex & Jenia                  Time: {0} ".format (clock))
    print ("################################################################################")
    print (" Segment:{0}\n DNS:{1} \n Gateway:{2}\n " .format (segment, dns_server, gateway))
    print ("################################################")
    print ("""              Menu
              ----
      """)


def display_main_menu():

    menu = {
        '1': 'Show all clients',
        '2': 'Send commands to all client',
        '3': 'Transfer file to clients all clients',
        '4': 'Install something on all clients',
        '5': 'Remove something from all clients',
    }
    for key, value in menu.iteritems():
        print(key, '.', value)


def display_agent_choice_menu():
    agents_list.display()


def dislay_menu(menu_level):
    if menu_level == 'main':
        display_main_menu()
    if menu_level == 'ag_list':
        display_agent_choice_menu()