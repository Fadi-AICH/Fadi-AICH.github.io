---
title: Python for Hacking — Getting Started
date: 2025-03-20
image: /assets/img/telechargement.png
categories:
  - Cyber Notes
  - Python Hacking
tags:
  - python
  - scripting
  - automation
  - hacking
toc: true
---
![]()

## Why Python for Hacking?

Python is the go-to language for security professionals because of its simplicity, vast library ecosystem, and rapid prototyping capability.

## Essential Libraries

```python
import socket       # Network connections
import requests     # HTTP requests
import subprocess   # System commands
import hashlib      # Hashing
import os           # OS interaction
```

## Simple Port Scanner

```python
import socket

target = "10.10.10.1"

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()
```

## HTTP Request Example

```python
import requests

url = "http://target.com/login"
data = {"username": "admin", "password": "test"}

response = requests.post(url, data=data)
print(response.status_code)
print(response.text[:500])
```

## Hash Cracking Basics

```python
import hashlib

wordlist = open("wordlist.txt", "r")
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

for word in wordlist:
    word = word.strip()
    if hashlib.md5(word.encode()).hexdigest() == target_hash:
        print(f"Found: {word}")
        break
```

## Next Steps

* Build a subdomain enumerator
* Write a brute-force script
* Automate Nmap scanning with `python-nmap`
