import socket
import threading
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()
    except Exception:
        pass

target = input("Enter target IP/domain: ")
for port in range(1, 1025):  # Scan ports 1-1024
    thread = threading.Thread(target=scan_port, args=(target, port))
    thread.start()