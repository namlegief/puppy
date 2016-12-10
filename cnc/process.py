import socket
import subprocess

agent_host = 'localhost'
agent_port = 4444

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socksize = 1024
conn.connect((agent_host, agent_port))

while True:
    shell = raw_input("$ ")
    conn.send(shell)
    data = conn.recv(socksize)
    # msglen = len(data)
    output = data
    iotype = subprocess.PIPE
    cmd = ['/bin/bash', '-c', shell]
    proc = subprocess.Popen(cmd, stdout=iotype).wait()
    stdout, stderr = proc.communicate()
    conn.send(stdout)
    print(output)
    if proc.returncode != 0:
        print("Error")