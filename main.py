import scapy.all as scapy

import scanner
import ip_finder

#Hide verbose
scapy.conf.verb = 0

print(scanner.scan("192.168.1.0/24"))


