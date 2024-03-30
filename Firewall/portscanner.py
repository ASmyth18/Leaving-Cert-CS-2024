import socket
import threading
from queue import Queue

target = input("Enter the target IP address: ")
port_range = input("Enter the port range to scan (e.g., 1-1000): ")
start_port, end_port = map(int, port_range.split('-'))

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    if result == 0:
        print(f"Port {port} is open")

def threader():
    while True:
        port = q.get()
        scan_port(port)
        q.task_done()

q = Queue()

for _ in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for port in range(start_port, end_port + 1):
    q.put(port)

q.join()