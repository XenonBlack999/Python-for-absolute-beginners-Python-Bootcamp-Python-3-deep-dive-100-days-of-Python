#ssh 
#paramiko ssh connection 

try:
    import os 
    import paramiko
except ImportError as e:
    print(f"Import failed: {e}")
finally:
    print("The importing section was done !")

    


def ssh_conn():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('ip', username='root',password='pass')
    stdin,stdout,stderr = ssh.exec_command("show version")
    output = stdout.read().decode('utf-8')
    print(output)
    # Run a command on the server and print the output
    stdin, stdout, stderr = ssh.exec_command("ls -l")
    print(stdout.read().decode())
    ssh.close()
    
try:
    ssh_conn()
except Exception as e:
    print(f"SSH connection failed: {e}")
    
ssh_conn()