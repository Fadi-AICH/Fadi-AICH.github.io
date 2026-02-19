---
title: Networking Basics for Hackers
date: 2025-03-10
image: /assets/img/digital-technology-social-network-global-connect-simple-business-logo-black-icon-on-white-background-vector.jpg
categories:
  - Cyber Notes
tags:
  - networking
  - tcp-ip
  - osi
  - dns
  - subnetting
toc: true
---
## The OSI Model

| Layer | Name        | Protocol Examples |
| ----- | ----------- | ----------------- |
| 7     | Application | HTTP, DNS, FTP    |
| 4     | Transport   | TCP, UDP          |
| 3     | Network     | IP, ICMP          |
| 2     | Data Link   | Ethernet, ARP     |
| 1     | Physical    | Cables, Wi-Fi     |

## TCP vs UDP

* **TCP**: Reliable, connection-oriented (3-way handshake: SYN → SYN-ACK → ACK)
* **UDP**: Fast, connectionless (used in DNS queries, streaming)

## IP Addressing & Subnetting

```
192.168.1.0/24 = 256 addresses (254 usable)
10.0.0.0/8    = Class A private range
172.16.0.0/12 = Class B private range
```

## Key Tools

* `nmap` — Network scanner and port mapper
* `Wireshark` — Packet capture and analysis
* `tcpdump` — CLI packet capture
* `traceroute` / `tracert` — Path tracing

## DNS

```bash
nslookup domain.com
dig domain.com ANY
```

Understanding DNS is critical for reconnaissance in penetration testing.
