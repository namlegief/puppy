import socket
import fcntl
import struct
import sys
# import pynetinfo

if_name = 'eth0'


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


netmask = get_netmask(if_name)
cidr = sum([bin(int(x)).count("1") for x in netmask.split(".")])
print('{}/{}'.format(get_ipv4_address(if_name), cidr))

def main():
    print('menu')
    print get_default_ipv4_gw()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('\nCommand interrupted')
        sys.exit(1)
