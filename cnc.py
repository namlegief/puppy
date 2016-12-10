import sys
from cnc import network
from cnc import time


if_name = 'wlp3s0'



def print_header(clock ,segment, dns_server,gateway ):
    print ("################################################################################")
    print ("  Python 102          Name: Alex & Jenia                  Time: {0} ".format (clock))
    print ("################################################################################")
    print (" Segment:{0}\n DNS:{1} \n Gateway:{2}\n " .format (segment, dns_server, gateway))
    print ("################################################")
    print ("""              Menu
              ----
      """)


def print_menu():
    menu = {
        '1': 'Show all clients',
        '2': 'Send commands to all client',
        '3': 'Transfer file to clients all clients',
        '4': 'Install something on all clients',
        '5': 'Remove something from all clients',
    }
    for key, value in menu.iteritems():
        print key, '.', value

    get_user_choice()


def get_user_choice():
    user_choice = raw_input("->:\n")
    print user_choice


def main():
    clock = time.get_current_time()
    segment = network.find_segment(if_name)
    gateway = network.get_default_ipv4_gw()
    dns_server = network.get_dns_server()
    print_header(clock, segment, dns_server,gateway)
    print_menu()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as err:
        print ('\nCommand interrupted').format(err.errno, err.strerror)
        sys.exit(err.errno)