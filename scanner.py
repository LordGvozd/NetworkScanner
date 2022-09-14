import scapy.all as scapy
import timer as t

def scan(ip):

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_requests = scapy.ARP(pdst=ip)

    arp_requests_broadcast = broadcast/arp_requests
    answered_list = scapy.srp(arp_requests_broadcast, timeout=1)[0]

    client_list = []
    for element in answered_list:
        client_list.append({"ip": element[1].psrc, "mac": element[1].hwsrc})

    return client_list

