---
title: Linux Fundamentals — Essential Commands
date: 2025-03-01
image: /assets/img/telechargement-1.png
categories:
  - Cyber Notes
  - Linux
tags:
  - linux
  - bash
  - commands
  - sysadmin
toc: true
---

## File System Navigation

```bash
pwd          # Print working directory
ls -la       # List all files with details
cd /path     # Change directory
find / -name "file.txt"  # Search for files
```

## File Permissions

Linux uses a permission model: **Owner / Group / Others** with **Read (4) / Write (2) / Execute (1)**.

```bash
chmod 755 script.sh    # rwxr-xr-x
chown user:group file  # Change ownership
```

## Process Management

```bash
ps aux       # List all processes
top          # Real-time process monitor
kill -9 PID  # Force kill a process
```

## Networking Commands

```bash
ifconfig / ip a    # Show network interfaces
netstat -tulpn     # Active connections
ss -tulpn          # Modern alternative
curl / wget        # Download files
```

## Essential for Pentesting

- `grep` — Search file contents
- `awk` / `sed` — Text processing
- `crontab -l` — Scheduled tasks (priv esc vector)
- `/etc/passwd` and `/etc/shadow` — User credential files
