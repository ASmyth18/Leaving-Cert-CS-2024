import socket
import threading
import requests
from scapy.all import *

# Basic socket programming
def basic_socket():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific IP and port
    server_socket.bind(('localhost', 8000))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 8000...")
    
    # Accept a client connection
    client_socket, address = server_socket.accept()
    print(f"Connected to client: {address}")
    
    # Send data to the client
    client_socket.send("Hello, client!".encode())
    
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(f"Received data from client: {data}")
    
    # Close the sockets
    client_socket.close()
    server_socket.close()

# Multithreaded server
def handle_client(client_socket):
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(f"Received data from client: {data}")
    
    # Send a response back to the client
    client_socket.send("Hello, client!".encode())
    
    # Close the client socket
    client_socket.close()

def multithreaded_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific IP and port
    server_socket.bind(('localhost', 8000))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print("Multithreaded server is listening on port 8000...")
    
    while True:
        # Accept a client connection
        client_socket, address = server_socket.accept()
        print(f"Connected to client: {address}")
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# HTTP requests
def http_requests():
    # Send a GET request
    response = requests.get("https://api.example.com/data")
    print(f"GET request status code: {response.status_code}")
    print(f"GET request content: {response.text}")
    
    # Send a POST request
    data = {'key': 'value'}
    response = requests.post("https://api.example.com/endpoint", json=data)
    print(f"POST request status code: {response.status_code}")
    print(f"POST request content: {response.text}")

# Packet sniffing and analysis
def packet_sniffing():
    # Sniff packets on the network
    packets = sniff(count=10)
    
    # Analyze the captured packets
    for packet in packets:
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")
        print("----")

# Main function
def main():
    print("Basic socket programming:")
    basic_socket()
    
    print("\nMultithreaded server:")
    multithreaded_server()
    
    print("\nHTTP requests:")
    http_requests()
    
    print("\nPacket sniffing and analysis:")
    packet_sniffing()

if __name__ == '__main__':
    main()