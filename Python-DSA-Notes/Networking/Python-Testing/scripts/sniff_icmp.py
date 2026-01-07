"""Sniff ICMP packets and print a short summary.
Requires scapy and elevated privileges.
"""
from scapy.all import sniff, ICMP


def handle(pkt):
    if pkt.haslayer(ICMP):
        print(pkt.summary())

if __name__ == '__main__':
    sniff(filter='icmp', prn=handle, count=0)  # count=0 => run until Ctrl+C
