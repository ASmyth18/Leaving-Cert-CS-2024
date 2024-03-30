from scapy.all import IP, TCP, UDP, send
import random
import time
import fw

def generate_normal_traffic():
    for _ in range(100):
        src_ip = f"10.0.0.{random.randint(1, 255)}"
        dst_ip = "192.168.1.100"
        sport = random.randint(1024, 65535)
        dport = 80
        packet = IP(src=src_ip, dst=dst_ip) / TCP(sport=sport, dport=dport)
        send(packet, verbose=False)
        time.sleep(0.1)

def generate_anomalous_traffic():
    src_ip = "192.168.1.200"
    dst_ip = "109.78.171.251"
    for _ in range(100):
        sport = random.randint(1024, 65535)
        dport = random.randint(1, 1024)
        packet = IP(src=src_ip, dst=dst_ip) / UDP(sport=sport, dport=dport)
        send(packet, verbose=False)
        time.sleep(0.01)

def test_anomaly_detection():
    generate_normal_traffic()
    generate_anomalous_traffic()

    # Wait for anomaly detection to process the traffic
    time.sleep(5)

    # Check if the anomalous IP is blocked
    anomalous_ip = "192.168.1.200"
    if anomalous_ip in fw.blocked_ips:
        print("Anomaly detection test passed!")
    else:
        print("Anomaly detection test failed.")

# Run the anomaly detection test
test_anomaly_detection()