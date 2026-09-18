# ARP Spoofing MITM Attack and Defense

**Student:** Hira Islam  
**Roll No:** BITF24M035  
**Course:** Information Security  
**Submitted to:** Huzaifa Nazir

This repository holds the academic materials for a **controlled lab** that studies Address Resolution Protocol (ARP) weaknesses, a Man-in-the-Middle (MITM) position on a local network, packet analysis, and **detection/defense**. Work is limited to VirtualBox virtual machines. It is not for use on real or public networks.

## Problem

LAN devices use ARP to map IP addresses to MAC addresses. Classic ARP does not authenticate replies, so a host can be tricked about who owns the gateway IP. This project shows that risk in an isolated lab, then shows how defenders can **detect** poisoned ARP mappings and reduce impact with encryption and network controls.

## Objectives

- Explain ARP and why unauthenticated replies are a problem
- Study MITM positioning between a victim VM and a gateway **in a private lab**
- Capture and compare **HTTP vs HTTPS** traffic with Wireshark
- Provide a **Python ARP monitor** that alerts on MAC/IP mismatches
- Document mitigations: HTTPS/VPN, static ARP, Dynamic ARP Inspection, monitoring, 2FA

## Lab environment (reference)

| Role | OS | Example IP | Notes |
|------|-----|------------|--------|
| Attacker VM | Kali Linux | `192.168.1.28` | Isolated lab only |
| Victim VM | Ubuntu | `192.168.1.27` | Isolated lab only |
| Gateway | Lab router | `192.168.1.1` | Lab topology |

Host platform: **VirtualBox** on Windows. Adapter settings used in the write-up: Bridged Adapter; attacker NIC promiscuous mode **Allow All** (lab VMs only).

**Do not** run these tools against networks you do not own or do not have written permission to test.

## Repository layout

Windows folder (this directory):

| File | Description |
|------|-------------|
| `BITF24M035_Project_Proposal.docx` | Project proposal |
| `MITM_Documentation.docx` | Full documentation |
| `MITM_Presentation.pptx` | Presentation slides |
| `README.md` | This file |


| File | Role in the project |
|------|---------------------|
| `arp_detect.py` | Defense: live ARP monitoring / mismatch alerts (Scapy) |
| `arp_spoof.py` | Lab automation used in the assignment (keep only for the report; do not reuse outside the lab) |
| `ip_forward.sh` | Lab helper related to IP forwarding on Kali |
| `attack_log.txt` | Detection / experiment log |
| `project_prAC.pcapng` | Wireshark capture for analysis (HTTP vs HTTPS discussion) |

## Tools mentioned in the documentation
Kali Linux, Ubuntu, VirtualBox, Wireshark, Python 3, Scapy, and lab utilities discussed in the report (Ettercap / `arpspoof`). Use them only inside the assigned VMs.

## Defense focus

- **Detection:** `arp_detect.py` watches ARP traffic and flags sender MAC values that do not match a known mapping; alerts can be written to a log.
- **Prevention:** HTTPS and VPN so intercepted bytes are not readable; static ARP on critical hosts; Dynamic ARP Inspection on managed switches; avoid sensitive work on untrusted Wi‑Fi; 2FA.

## Ethics

This work is **course-only**, **VM-only**, and **authorized-lab-only**. Capturing or altering traffic on production, campus, or other people’s networks without permission is illegal.

## References

- [Ettercap](https://www.ettercap-project.org)
- [Wireshark documentation](https://www.wireshark.org/docs)
- [OWASP](https://owasp.org)
- [Scapy](https://scapy.net)
- [Kali Linux docs](https://www.kali.org/docs)

See `MITM_Documentation.docx` for the full write-up and results table.
