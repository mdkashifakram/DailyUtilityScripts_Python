import socket
import requests

def check_open_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for the connection
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def check_weak_password(ip, port, common_passwords):
    for password in common_passwords:
        try:
            response = requests.get(f"http://{ip}:{port}/login", auth=("admin", password), timeout=3)
            if response.status_code == 200:
                print(f"Router has a weak password: {password}")
                return True
        except requests.RequestException:
            continue
    return False

def main():
    # Router's IP, usually the gateway IP, e.g., '192.168.1.1'
    router_ip = "192.168.1.1"
    # Common router management ports and services
    ports_to_check = [80, 443, 23, 21, 22, 8080]
    # List of common passwords to try
    common_passwords = ["admin", "password", "123456", "1234", "admin123", "root", "guest"]
    
    # Check for open ports
    open_ports = check_open_ports(router_ip, ports_to_check)
    if open_ports:
        print(f"Open ports found on {router_ip}: {open_ports}")
    else:
        print(f"No open ports found on {router_ip}.")

    # Check for weak passwords on open ports
    for port in open_ports:
        if check_weak_password(router_ip, port, common_passwords):
            print(f"Weak password found on port {port}")
            break
    else:
        print("No weak passwords found on open ports.")

if __name__ == "__main__":
    main()
