#!/usr/bin/python
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, gethostbyaddr, error

from thread import start_new_thread

from os import system

import get_time

from time import sleep

import network

from sys import exit as exitapp

host = ''

port = 1234

buffer_size = 4096

connections = []

max_connections = 5

sock = socket(AF_INET, SOCK_STREAM)

sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

try:

    sock.bind((host, port))

except error as msg:

    # debug level

    # print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

    print "Socket Error: %s" % msg

    exitapp()

sock.listen(max_connections)


def GetConnections():
    num = 1

    for client in connections:
        ip = client[1][0]

        hostname = gethostbyaddr(ip)[0]

        print "%s) ip %s - %s" % (num, ip, hostname)

        num += 1


def ShowClients():
    print "Clients:"

    GetConnections()

    EnterToMenu()


def SendCommand():
    GetConnections()

    inp = int(raw_input("Enter Client Number or 0 for all "))

    com = raw_input("Enter Command: ")

    if inp == 0:

        for i in connections:

            try:

                i[0].send(com)

                print(i[1], " success")

                sleep(1)

                print(i[0].recv(buffer_size))

            except:

                print(i[1], " failed")

                connections.remove(i)

                break

    else:

        try:

            connections[inp - 1][0].send(com)

            print(connections[inp - 1][1], "success")

            print(connections[inp - 1][0].recv(buffer_size))

        except:

            print(connections[inp - 1][1], "failed")

            connections.remove(connections[inp - 1])

            return

    EnterToMenu()


def SendFile():
    GetConnections()

    inp = int(raw_input("Enter Client Number or 0 for all "))

    sourcefile = raw_input("Enter Source ")

    destination = raw_input("Enter Destination ")

    if inp == 0:

        for i in connections:

            try:

                i[0].send("F")

                print(i[1], " success")

            except:

                print(i[1], " failed")

                connections.remove(i)

                break

            sleep(1)

            i[0].send(destination)

            f = open(sourcefile, 'rb')

            l = f.read(1024)

            while (l):
                i[0].send(l)

                l = f.read(1024)

            f.close()

            i[0].send("E")

    else:

        try:

            connections[inp - 1][0].send("F")

            print(connections[inp - 1][1], "success")

        except:

            print(connections[inp - 1][1], " failed")

            connections.remove(connections[inp - 1])

            return

        sleep(1)

        connections[inp - 1][0].send(destination)

        f = open(sourcefile, 'rb')

        l = f.read(1024)

        while (l):
            connections[inp - 1][0].send(l)

            l = f.read(1024)

        f.close()

        sleep(1)

        connections[inp - 1][0].send("E")

    EnterToMenu()


def InstallAndRemove(TypeAction):
    GetConnections()

    inp = int(raw_input("Enter Client Number or 0 for all "))

    program = raw_input("Enter Source Program ")

    actioncmd = "apt-get -y %s %s" % (TypeAction, program)

    if inp == 0:

        for i in connections:

            try:

                i[0].send("package")

                print(i[1], " success")

            except:

                print(i[1], " failed")

                connections.remove(i)

                break

            sleep(1)

            i[0].send(actioncmd)

    else:

        try:

            connections[inp - 1][0].send("package")

            print(connections[inp - 1][1], " success")

        except:

            print(connections[inp - 1][1], " failed")

            connections.remove(connections[inp - 1])

            return

        sleep(1)

        connections[inp - 1][0].send(actioncmd)

    EnterToMenu()


def ShellAcsess():
    GetConnections()

    inp = int(raw_input("Enter Client Number "))

    print "Remmber Enter exit, to close the exit!"

    while True:

        commandtosend = raw_input("-> ")

        if (commandtosend == "exit"):
            print "Exiting...."

            EnterToMenu()

        try:

            connections[inp - 1][0].send("shell")

            connections[inp - 1][0].send(commandtosend)

            print(connections[inp - 1][0].recv(buffer_size))

        except:

            print(connections[inp - 1][1], " failed")

            connections.remove(connections[inp - 1])

            return

    sleep(1)

    EnterToMenu()


def NotFound():
    print "Option not found!"

    menu(a=1)


def EnterToMenu():

    try:
        input("Hit Enter to Back Menu..")
        fail
    except:
        menu(1)


nic = 'wlp3s0'
clock = get_time.get_current_time()
segment = network.find_segment(nic)
gateway = network.get_default_ipv4_gw()
dns_server = ', '.join(network.get_dns_server())

def menu(a):
    system("clear")

    print ("################################################################################")
    print ("  Python 102          Name: Alex & Jenia                  Time: {0} ".format(clock))
    print ("################################################################################")
    print (" Segment:{0}\n DNS:{1} \n Gateway:{2} ".format(segment, dns_server, gateway))
    print ("################################################")
    print ("""              Menu
              ----
        1) Show clients
        2) Send commands
        3) File Transfer
        4) Installion
        5) Remove
        6) Shell on a client """
           )

    user_chose = raw_input("Chose Options -> ")

    choice = {

        "1": ShowClients,

        "2": SendCommand,

        "3": SendFile,

        "4": lambda: InstallAndRemove(TypeAction="install"),

        "5": lambda: InstallAndRemove(TypeAction="remove"),

        "6": ShellAcsess

    }

    choice.get(user_chose, NotFound)()


start_new_thread(menu, (1,))

while True:
    conn, addr = sock.accept()

    connections.append([conn, addr])

sock.close()
