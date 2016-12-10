import socket
import fcntl
import struct
import sys
import datetime
# import pynetinfo
resolvers = []
if_name = 'wlp3s0'


def get_current_time():
    now = datetime.datetime.now()
    clock = now.strftime("%H:%M")
    return clock


def get_ipv4_address(if_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                        0x8915,  # SIOCGIFADDR
                                        struct.pack('256s', if_name[:15])
                                        )[20:24])


def get_netmask(if_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                                        0x891b,
                                        struct.pack('256s', if_name)
                                        )[20:24])


def get_default_ipv4_gw():
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[2] != '00000000' or not int(fields[3], 16) & 2:
                continue
        return socket.inet_ntoa(struct.pack("<L", int(fields[1], 16)))


def find_segment(if_name):
    netmask = get_netmask(if_name)
    cidr = sum([bin(int(x)).count("1") for x in netmask.split(".")])
    segment = ('{}/{}'.format(get_ipv4_address(if_name), cidr))
    return segment


def get_dns_server():
    with(open('/etc/resolv.conf')) as rc:
        ns_re = re.compile(r'^nameserver (.+)$')
        for line in rc:
            if ns_re.match(line):
                tokens = line.split(' ')
                resolvers.append(tokens[1].strip())
    return resolvers


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
    clock = get_current_time()
    segment = find_segment(if_name)
    gateway = get_default_ipv4_gw()
    dns_server = get_dns_server()
    print_header(clock, segment, dns_server,gateway)
    print_menu()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('\nCommand interrupted')
sys.exit(1)


