from scapy.all import rdpcap

def process_pcap(filename):
    packets = rdpcap(filename)
    for packet in packets:
        print(packet.summary())  

process_pcap('packets.pcap')
