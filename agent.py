import sys
import socket
import subprocess
import tools

config = tools.parse_config()

socksize = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((config['agent_host'], int(config['agent_port'])))
print("Server started on port: {}".format(config['agent_port']))

server.listen(1)
print("Agent started\n")
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