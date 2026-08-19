from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


def process_packet(packet):
    print("\n" + "=" * 70)

    # Capture time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Time       : {timestamp}")

    # Check IP packet
    if IP in packet:

        # Source and destination IP
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        print(f"Source IP  : {source_ip}")
        print(f"Dest. IP   : {destination_ip}")

        # TCP packet
        if TCP in packet:
            print("Protocol   : TCP")
            print(f"Src Port   : {packet[TCP].sport}")
            print(f"Dst Port   : {packet[TCP].dport}")

        # UDP packet
        elif UDP in packet:
            print("Protocol   : UDP")
            print(f"Src Port   : {packet[UDP].sport}")
            print(f"Dst Port   : {packet[UDP].dport}")

        # ICMP packet
        elif ICMP in packet:
            print("Protocol   : ICMP")

        # Other IP protocol
        else:
            print("Protocol   : Other IP")

        # Packet data
        if Raw in packet:
            data = bytes(packet[Raw].load)

            readable_data = data.decode(
                "utf-8",
                errors="replace"
            )

            print(f"Packet Data: {readable_data[:100]}")

        else:
            print("Packet Data: No application data")

    else:
        print("Non-IP packet captured")


# Program heading
print("=" * 70)
print("             CODSOFT - NETWORK PACKET ANALYZER")
print("=" * 70)

print("\nCapturing 20 packets...")
print("Generate network activity by opening a website.")
print("The program will automatically stop after 20 packets.\n")


# Capture 20 packets
try:
    sniff(
        prn=process_packet,
        count=20,
        store=False
    )

    print("\n" + "=" * 70)
    print("Packet capture completed successfully.")
    print("Total packets captured: 20")
    print("=" * 70)

except KeyboardInterrupt:
    print("\n\nPacket capture stopped by user.")

except Exception as e:
    print("\nError:", e)