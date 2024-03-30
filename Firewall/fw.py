# Import necessary libraries
from scapy.all import *  # Import all functions and classes from Scapy
import logging  # Import the logging module for logging purposes
from datetime import datetime  # Import the datetime class for timestamping
from collections import defaultdict  # Import defaultdict for managing counters efficiently
import threading  # Import threading for concurrent execution
import numpy as np  # Import numpy for numerical operations
import time  # Import time for time-related operations
import requests  # Import requests for HTTP requests
from sklearn.neighbors import LocalOutlierFactor  # Import LocalOutlierFactor for anomaly detection

# Configure logging
logging.basicConfig(filename='firewall.log', level=logging.INFO, format='%(asctime)s - %(message)s')
# Set up logging to write to 'firewall.log' file with timestamp and message format

# Firewall rules
allowed_ports = [80, 443, 22]  # Define list of allowed ports (HTTP, HTTPS, SSH)
blocked_ips = ["10.0.0.5", "192.168.1.100", "192.168.1.200"]  # Define list of blocked IP addresses
allowed_protocols = ["TCP", "UDP", "ICMP"]  # Define list of allowed protocols
allowed_ips = []  # Initialize empty list for dynamically allowed IP addresses

# NAT configuration
nat_table = {"192.168.1.10": "public_ip_1", "192.168.1.20": "public_ip_2"}
# Define NAT mappings for private IP addresses to public IP addresses

syn_flood_threshold = 100  # Set threshold for SYN flood detection
port_scan_threshold = 50  # Set threshold for port scan detection
ddos_threshold = 1000  # Set threshold for DDoS detection

syn_flood_counter = defaultdict(int)  # Initialize counter for SYN flood attacks
port_scan_counter = defaultdict(int)  # Initialize counter for port scan attacks
ddos_counter = defaultdict(int)  # Initialize counter for DDoS attacks

# Anomaly detection model
anomaly_detector = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
anomaly_data = []  # Initialize list for anomaly detection data

# Function to retrieve current IP address
def get_current_ip():
    try:
        response = requests.get('https://api.ipify.org')  # Send GET request to retrieve public IP address
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.text.strip()  # Return stripped IP address
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve current IP address: {e}")  # Log error if IP retrieval fails
        return None

# Function to update allowed IPs
def update_allowed_ips():
    current_ip = get_current_ip()  # Get current public IP address
    if current_ip:
        allowed_ips.append(current_ip)  # Add current IP address to allowed IPs list
        logging.info(f"Updated allowed IPs: {allowed_ips}")  # Log updated list of allowed IPs

# Packet filtering function
def packet_filter(packet):
    if packet.haslayer(IP):  # Check if packet has IP layer
        src_ip = packet[IP].src  # Get source IP address
        dst_ip = packet[IP].dst  # Get destination IP address
        protocol = packet[IP].proto  # Get protocol

        # Allow traffic from allowed IP addresses
        if src_ip in allowed_ips:
            return True

        # Block traffic from specific IP addresses
        if src_ip in blocked_ips:
            logging.warning(f"Blocked packet from {src_ip} to {dst_ip}")  # Log blocked packet
            return False

        # Allow outgoing traffic
        if src_ip.startswith("109.76.161.91"):
            return True

        # Block incoming traffic on specific ports
        if packet.haslayer(TCP) and packet[TCP].dport not in allowed_ports:
            logging.warning(f"Blocked incoming TCP traffic on port {packet[TCP].dport}")  # Log blocked TCP traffic
            return False
        if packet.haslayer(UDP) and packet[UDP].dport not in allowed_ports:
            logging.warning(f"Blocked incoming UDP traffic on port {packet[UDP].dport}")  # Log blocked UDP traffic
            return False

        # Block unsupported protocols
        if protocol not in allowed_protocols:
            logging.warning(f"Blocked traffic with unsupported protocol: {protocol}")  # Log blocked traffic
            return False

    return True

# NAT translation function
def nat_translate(packet):
    if packet.haslayer(IP):  # Check if packet has IP layer
        src_ip = packet[IP].src  # Get source IP address
        if src_ip in nat_table:
            packet[IP].src = nat_table[src_ip]  # Translate source IP address
            logging.info(f"Translated source IP: {src_ip} to {nat_table[src_ip]}")  # Log NAT translation
    return packet

# Logging function
def log_packet(packet):
    if packet.haslayer(IP):  # Check if packet has IP layer
        src_ip = packet[IP].src  # Get source IP address
        dst_ip = packet[IP].dst  # Get destination IP address
        protocol = packet[IP].proto  # Get protocol
        logging.info(f"Source: {src_ip}, Destination: {dst_ip}, Protocol: {protocol}")  # Log packet details

# Function to detect SYN flood attacks
def detect_syn_flood(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == "S":  # Check if packet is TCP SYN packet
        src_ip = packet[IP].src  # Get source IP address
        syn_flood_counter[src_ip] += 1  # Increment SYN flood counter for source IP
        if syn_flood_counter[src_ip] > syn_flood_threshold:  # Check if threshold exceeded
            logging.critical(f"Potential SYN flood attack detected from {src_ip}")  # Log SYN flood attack
            # Block the source IP for a certain duration
            blocked_ips.append(src_ip)
            threading.Timer(60, remove_blocked_ip, args=(src_ip,)).start()  # Schedule IP removal

# Function to detect port scan attacks
def detect_port_scan(packet):
    if packet.haslayer(IP):  # Check if packet has IP layer
        if packet.haslayer(TCP) or packet.haslayer(UDP):  # Check if packet is TCP or UDP
            src_ip = packet[IP].src  # Get source IP address
            port_scan_counter[src_ip] += 1  # Increment port scan counter for source IP
            if port_scan_counter[src_ip] > port_scan_threshold:  # Check if threshold exceeded
                logging.critical(f"Potential port scan detected from {src_ip}")  # Log port scan attack
                # Block the source IP for a certain duration
                blocked_ips.append(src_ip)
                threading.Timer(120, remove_blocked_ip, args=(src_ip,)).start()  # Schedule IP removal

# Function to detect DDOS attacks
def detect_ddos(packet):
    if packet.haslayer(IP):  # Check if packet has IP layer
        src_ip = packet[IP].src  # Get source IP address
        ddos_counter[src_ip] += 1  # Increment DDoS counter for source IP
        if ddos_counter[src_ip] > ddos_threshold:  # Check if threshold exceeded
            logging.critical(f"Potential DDoS attack detected from {src_ip}")  # Log DDoS attack
            # Block the source IP for a certain duration
            blocked_ips.append(src_ip)
            threading.Timer(300, remove_blocked_ip, args=(src_ip,)).start()  # Schedule IP removal

# Function to detect anomalies using machine learning
def detect_anomalies(packet):
    if packet.haslayer(IP):  # Check if packet has IP layer
        src_ip = packet[IP].src  # Get source IP address
        features = [syn_flood_counter[src_ip], port_scan_counter[src_ip], ddos_counter[src_ip]]
        # Gather features for anomaly detection
        anomaly_data.append(features)  # Add features to anomaly data
        if len(anomaly_data) >= 100:  # Check if enough data points collected
            X = np.array(anomaly_data)  # Convert data to numpy array
            anomaly_scores = anomaly_detector.fit_predict(X)  # Detect anomalies
            outlier_indices = np.where(anomaly_scores == -1)[0]  # Get indices of outliers
            for index in outlier_indices:
                anomaly_src_ip = anomaly_data[index][0]  # Get source IP of anomaly
                logging.critical(f"Anomaly detected from {anomaly_src_ip}")  # Log anomaly
                # Block the source IP for a certain duration
                blocked_ips.append(anomaly_src_ip)
                threading.Timer(300, remove_blocked_ip, args=(anomaly_src_ip,)).start()  # Schedule IP removal
            anomaly_data.clear()  # Clear anomaly data

# Helper function to remove blocked IP after certain duration
def remove_blocked_ip(ip):
    blocked_ips.remove(ip)  # Remove IP from blocked list
    logging.info(f"Removed {ip} from blocked IPs list")  # Log IP removal

# Function to reset counters periodically
def reset_counters():
    syn_flood_counter.clear()  # Clear SYN flood counter
    port_scan_counter.clear()  # Clear port scan counter
    ddos_counter.clear()  # Clear DDoS counter

# Function to process packets
def process_packets():
    sniff(prn=lambda packet: process_packet(packet), store=False)  # Sniff packets and process each one

# Function to process individual packet
def process_packet(packet):
    if packet_filter(packet):  # Check if packet passes filtering rules
        packet = nat_translate(packet)  # Translate packet using NAT
        log_packet(packet)  # Log packet details
        detect_syn_flood(packet)  # Detect SYN flood attacks
        detect_port_scan(packet)  # Detect port scan attacks
        detect_ddos(packet)  # Detect DDoS attacks
        send(packet)  # Send processed packet

# Function to perform periodic tasks
def periodic_tasks():
    while True:
        update_allowed_ips()  # Update allowed IPs
        reset_counters()  # Reset counters
        time.sleep(300)  # Wait for 5 minutes before next update

# Function to start the firewall
def start_firewall():
    logging.info("Firewall started")  # Log firewall start
    threading.Thread(target=periodic_tasks).start()  # Start periodic tasks in separate thread
    process_packets()  # Start packet processing

# Main entry point
if __name__ == "__main__":
    start_firewall()  # Start the firewall
                
