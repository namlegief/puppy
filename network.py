import socket
import struct
import fcntl
import re

resolvers = []


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
