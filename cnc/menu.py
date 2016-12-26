import tools
from thread import start_new_thread
from cnc import network
from cnc import time


config = tools.get_bind_settings()

def ShowClients():
    print 'show'
    EnterToMenu()


def SendCommand():
    print 'send'
    EnterToMenu()


def SendFile():
    print 'sendfile'
    EnterToMenu()


def install():
    print 'install'
    EnterToMenu()


def remove():
    print 'remove'
    EnterToMenu()


def ShellAccess():
    print 'shell'
    EnterToMenu()


def NotFound():
    print "Option not found!"
    menu(arg=1)


def EnterToMenu():
    try:
        input("Hit Enter to Back Menu..")
    except:
        menu(arg=1)



def menu(arg=False):
    clock = time.get_current_time()
    segment = network.find_segment(config['cnc_if_name'])
    gateway = network.get_default_ipv4_gw()
    dns_server = network.get_dns_server()

    print ("################################################################################")
    print ("  Python 102          Name: Alex & Jenia                  Time: {0} ".format(clock))
    print ("################################################################################")
    print (" Segment:{0}\n DNS:{1} \n Gateway:{2}\n ".format(segment, dns_server, gateway))
    print ("################################################")
    print ("""              Menu
                  ----
          """)
    print """
        ################################################################
        #       Python 102          Name: The girl has no name:)       #
        ################################################################
        1) Show clients
        2) Send commands
        3) File Transfer
        4) Installion
        5) Remove
        6) Shell on a client """

    userChose = raw_input("Choose Options -> ")
    choice = {
        "1": ShowClients,
        "2": SendCommand,
        "3": SendFile,
        "4": install,
        "5": remove,
        "6": ShellAccess
    }
    choice.get(userChose, NotFound)()


if __name__ == '__main__':

    try:

        start_new_thread(menu(), ('',))

    except Exception, err:
        print err