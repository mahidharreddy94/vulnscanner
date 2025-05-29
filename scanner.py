# Automated Vulnerability Scanner
import socket
import threading

# Common ports to scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} open on {ip}")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port} on {ip}: {e}")

def scan_target(ip):
    print(f"[*] Scanning target: {ip}")
    threads = []
    for port in common_ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    scan_target(target_ip)
