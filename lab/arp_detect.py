#!/usr/bin/env python3
# ARP Spoofing Detection Script
# Defense Tool - MITM Project
# Author: Hira Islam

from scapy.all import sniff, ARP
import datetime
import os

print("=" * 45)
print("    ARP Guard - Detection Tool      ")
print("    MITM Project - Defense Phase    ")
print("=" * 45)

# Aapki image se liye gaye sahi IP aur MAC addresses
LEGITIMATE = {
    "192.168.0.107": "08:00:27:fb:b3:c1",  # Ubuntu VM
    "192.168.0.108": "08:00:27:6f:d5:be",  # Kali VM
    "192.168.0.1": "cc:2d:21:30:98:10",    # Gateway/Router
}

LOG_FILE = "attack_log.txt"

def log_attack(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write("[" + timestamp + "] " + msg + "\n")
    print("[LOG SAVED] " + LOG_FILE)

def detect_arp(packet):
    if packet.haslayer(ARP):
        # op=2 ka matlab hai ARP Reply packet
        if packet[ARP].op == 2:
            sender_ip  = packet[ARP].psrc
            sender_mac = packet[ARP].hwsrc

            if sender_ip in LEGITIMATE:
                real_mac = LEGITIMATE[sender_ip]

                if sender_mac != real_mac:
                    alert = (
                        "\n[ALERT] ARP SPOOFING DETECTED!\n"
                        "IP      : " + sender_ip + "\n"
                        "Real MAC: " + real_mac + "\n"
                        "Fake MAC: " + sender_mac + "\n"
                        "WARNING : MITM ATTACK IN PROGRESS!"
                    )
                    print(alert)
                    log_attack(alert)
                else:
                    # Optional: Aap isay hata bhi sakte hain agar sirf alerts dekhne hain
                    print(f"[SAFE] {sender_ip} is at {sender_mac}")

print("[*] Monitoring network on eth0...")
print("[*] Press Ctrl+C to stop\n")

# Ubuntu par interface ka naam 'enp0s3' ho sakta hai
# Kali par 'eth0' hota hai. Aap 'eth0' try karein:
sniff(filter="arp", prn=detect_arp, store=0)
