---
layout: post
title: "Tanger Med — Network Security Monitoring"
date: 2025-09-15
categories: [Projects, Cybersecurity, Networking]
tags: [SELKS, Suricata, Zeek, Cisco, Kibana, IDS]
image: /assets/img/tanger-med/tanger-med-p48.jpg
excerpt: "Tanger Med internship project: passive Cisco traffic acquisition feeding a SELKS-based NSM stack with Suricata, Zeek, Elasticsearch/Kibana and Scirius."
---

<style>.case-hero{border:1px solid var(--border-color);border-radius:18px;overflow:hidden;margin-bottom:1.5rem}.case-hero img{width:100%;display:block}.case-callout{padding:1rem 1.2rem;border-left:3px solid var(--accent);background:rgba(56,189,248,.06);margin:1.2rem 0}.case-gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}.case-gallery figure{margin:0;border:1px solid var(--border-color);border-radius:12px;overflow:hidden;background:var(--bg-card)}.case-gallery img{width:100%;display:block}.case-gallery figcaption{padding:.65rem;font-size:.78rem;color:var(--text-secondary)}.case-btn{display:inline-block;padding:.6rem .9rem;border:1px solid var(--accent);border-radius:10px;font-weight:700;margin:.4rem .4rem .4rem 0}@media(max-width:700px){.case-gallery{grid-template-columns:1fr}}</style>

<div class="case-hero"><img src="{{ '/assets/img/tanger-med/tanger-med-p48.jpg' | relative_url }}" alt="Tanger Med NSM project"></div>

During my cybersecurity/network-monitoring internship at **Tanger Med Port Authority**, I designed and deployed a passive Network Security Monitoring chain combining Cisco traffic mirroring with the SELKS ecosystem.

<div class="case-callout"><strong>Functional chain:</strong> Cisco SPAN/RSPAN → Suricata + Zeek → Elasticsearch → Kibana → SOC investigation, with Scirius for Suricata rule governance.</div>

## Architecture & implementation

The project covered VLAN/PVLAN and trunk design, SPAN-based acquisition, SELKS deployment, Suricata signature detection, Zeek behavioral/network analysis and centralized Elastic/Kibana investigation.

<div class="case-gallery">
<figure><img src="{{ '/assets/img/tanger-med/tanger-med-p30.jpg' | relative_url }}" alt="NSM tooling"><figcaption>NSM tooling and deployment context.</figcaption></figure>
<figure><img src="{{ '/assets/img/tanger-med/tanger-med-p34.jpg' | relative_url }}" alt="NSM architecture"><figcaption>Target passive-monitoring architecture.</figcaption></figure>
<figure><img src="{{ '/assets/img/tanger-med/tanger-med-p38.jpg' | relative_url }}" alt="SELKS"><figcaption>SELKS / sensor implementation evidence.</figcaption></figure>
<figure><img src="{{ '/assets/img/tanger-med/tanger-med-p42.jpg' | relative_url }}" alt="Suricata Zeek"><figcaption>Network detection and telemetry workflow.</figcaption></figure>
<figure><img src="{{ '/assets/img/tanger-med/tanger-med-p48.jpg' | relative_url }}" alt="Kibana"><figcaption>Visualization and SOC investigation evidence.</figcaption></figure>
<figure><img src="{{ '/assets/img/tanger-med/tanger-med-p54.jpg' | relative_url }}" alt="Validation"><figcaption>Operational validation evidence.</figcaption></figure>
</div>

## What the project demonstrates

- Passive traffic visibility through Cisco **SPAN/RSPAN**.
- Segmentation concepts using **VLANs, trunks and PVLANs**.
- **Suricata** signature-based IDS monitoring.
- **Zeek** behavioral/network metadata visibility.
- Centralized indexing with **Elasticsearch** and investigation with **Kibana**.
- **Scirius** rule governance.
- Controlled validation scenarios including scans, brute-force and exfiltration-oriented testing.

This public case study is intentionally sanitized: it presents the architecture and engineering work without exposing sensitive operational details of a critical port environment.

<a class="case-btn" href="https://github.com/Fadi-AICH/tanger-med-network-security-monitoring" target="_blank">GitHub repository ↗</a>
<a class="case-btn" href="{{ '/projects/' | relative_url }}">All projects</a>
