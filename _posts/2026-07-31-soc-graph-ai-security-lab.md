---
layout: post
title: "SOC Graph AI — Detection, Correlation & SOAR"
date: 2026-07-31
permalink: /projects/soc-graph-ai/
categories: [Projects, Cybersecurity]
tags: [Wazuh, Neo4j, MITRE-ATTACK, SOAR, Detection-Engineering, Python]
image: /assets/img/nearsecure/nearsecure-p48.jpg
excerpt: "NearSecure internship project: an end-to-end SOC lab connecting Wazuh detections, MITRE enrichment, UEBA/ML, Neo4j graph correlation, analyst dashboards and approval-gated SOAR."
---

<style>.case-hero{border:1px solid var(--border-color);border-radius:18px;overflow:hidden;margin-bottom:1.5rem}.case-hero img{width:100%;display:block}.case-callout{padding:1rem 1.2rem;border-left:3px solid var(--accent);background:rgba(56,189,248,.06);margin:1.2rem 0}.case-gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}.case-gallery figure{margin:0;border:1px solid var(--border-color);border-radius:12px;overflow:hidden;background:var(--bg-card)}.case-gallery img{width:100%;display:block}.case-gallery figcaption{padding:.65rem;font-size:.78rem;color:var(--text-secondary)}.case-btn{display:inline-block;padding:.6rem .9rem;border:1px solid var(--accent);border-radius:10px;font-weight:700;margin:.4rem .4rem .4rem 0}@media(max-width:700px){.case-gallery{grid-template-columns:1fr}}</style>
<div class="case-hero"><img src="{{ '/assets/img/nearsecure/nearsecure-p48.jpg' | relative_url }}" alt="SOC Graph AI project evidence"></div>
This NearSecure internship project was built around one idea: **a security event should remain traceable from detection to analyst decision**. The laboratory connects controlled adversary activity to Wazuh, a Python analytics pipeline, MITRE ATT&CK enrichment, local UEBA/ML scoring, Neo4j graph correlation, Streamlit analyst views and approval-gated n8n/Shuffle workflows.
<div class="case-callout"><strong>Final validated dataset:</strong> 1,396 alerts. The project demonstrates the full evidence chain—controlled activity → detection → normalized/enriched data → graph relationship → risk score → analyst view → controlled triage.</div>
## Architecture
The controlled `192.168.56.0/24` laboratory included Windows/Sysmon, Linux, Kali/Caldera, pfSense and Wazuh. The host ran the Python pipeline, Neo4j, Streamlit, n8n and Shuffle.
<div class="case-gallery"><figure><img src="{{ '/assets/img/nearsecure/nearsecure-p20.jpg' | relative_url }}" alt="SOC architecture"><figcaption>Architecture and data-flow design.</figcaption></figure><figure><img src="{{ '/assets/img/nearsecure/nearsecure-p30.jpg' | relative_url }}" alt="Wazuh implementation"><figcaption>Wazuh collection and detection implementation.</figcaption></figure><figure><img src="{{ '/assets/img/nearsecure/nearsecure-p36.jpg' | relative_url }}" alt="Detection validation"><figcaption>Controlled detection and validation evidence.</figcaption></figure><figure><img src="{{ '/assets/img/nearsecure/nearsecure-p48.jpg' | relative_url }}" alt="Graph AI"><figcaption>Graph/analytics evidence from the SOC workflow.</figcaption></figure><figure><img src="{{ '/assets/img/nearsecure/nearsecure-p52.jpg' | relative_url }}" alt="Analyst dashboard"><figcaption>Analyst-facing correlation and prioritization views.</figcaption></figure><figure><img src="{{ '/assets/img/nearsecure/nearsecure-p64.jpg' | relative_url }}" alt="Final validation"><figcaption>Final validation and end-to-end SOC evidence.</figcaption></figure></div>
## Engineering scope
- **Detection:** Wazuh, Sysmon, Linux telemetry and pfSense logs.
- **Adversary validation:** manual controlled scenarios, Atomic Red Team and Caldera.
- **Analytics:** Python normalization, MITRE enrichment and local UEBA/ML prioritization.
- **Correlation:** Neo4j relationships across alerts, hosts, users, IPs, processes, rules and ATT&CK techniques.
- **Analyst experience:** Streamlit views for overview, MITRE, risk, ML and graph evidence.
- **Response:** n8n and Shuffle workflows designed to remain approval-gated.

The project deliberately does **not** claim production-grade ML generalization or completed automated pfSense blocking. Those remain future improvements requiring broader validation and safe approval/rollback controls.

<a class="case-btn" href="https://github.com/Fadi-AICH/soc-graph-ai-security-lab" target="_blank">GitHub repository ↗</a> <a class="case-btn" href="{{ '/projects/' | relative_url }}">All projects</a>
