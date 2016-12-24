#!/usr/bin/python
from thread import start_new_thread
from sys import *
import time


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
    menu(a=1)


def EnterToMenu():
    try:
        input("Hit Enter to Back Menu..")
    except:
        menu(a=1)


def menu(a):
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
        
        start_new_thread(menu,(77,))

    except Exception, errtxt:
                print errtxt

    time.sleep(5)
