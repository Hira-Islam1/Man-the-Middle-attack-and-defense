#!/bin/bash
# IP Forwarding Enable Script
# Yeh script Kali ko router ki
# tarah kaam karne deti hai
# Author: [Aapka Naam]
# Date: [Date]

echo "========================================="
echo "        MITM Attack - IP Forwarding      "
echo "========================================="

# IP Forwarding enable karo
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Verify karo
STATUS=$(cat /proc/sys/net/ipv4/ip_forward)

if [ "$STATUS" -eq 1 ]; then
    echo "[✅] IP Forwarding: ENABLED"
else
    echo "[❌] IP Forwarding: FAILED"
fi

echo "========================================="
