# Python for Networking & Security — Overview

## 1. Common libraries and what they're good for
- scapy — packet crafting, sniffing, manipulation (great for protocol experiments).
- pyshark — Python wrapper for tshark (packet analysis without C bindings).
- socket — low-level networking, useful for simple clients/servers and lightweight scans.
- paramiko / netmiko — SSH automation and device management.
- python-nmap / libnmap — controlling Nmap from Python for discovery.
- requests / urllib3 — HTTP requests, useful for probing web services.
- pysnmp — SNMP interactions.
- scikit-learn / tensorflow / pytorch — building ML models for anomaly detection.

## 2. Safe example snippets

### Packet sniffing (scapy)
```python
# requires: scapy (run as admin/root to sniff on interfaces)
from scapy.all import sniff

def handle(pkt):
    if pkt.haslayer('IP'):
        print(pkt.summary())

# sniff 10 packets and call handler
sniff(count=10, prn=handle)
```

### Simple TCP port probe (ethical, non-invasive)
```python
import socket

def probe(host, port, timeout=1.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except Exception:
            return False

print(probe('scanme.nmap.org', 22))
```

### HTTP header probe (requests)
```python
import requests

r = requests.get('https://example.com', timeout=5)
print(r.status_code)
print(r.headers.get('Server'))
```

## 3. Testing vs offensive actions — ethics & legal
- Port scanning and probing are dual-use; only perform with permission.
- Do not include or run brute-force / password cracking scripts here.

## 4. Automation & network engineering workflows
- Use Paramiko/Netmiko for SSH-based automation, Ansible for declarative automation, Napalm for multi-vendor network changes.

## 5. ML/AI for network security
- Use flow features (NetFlow) or packet-derived features to feed models.
- Typical tasks: anomaly detection (autoencoders, isolation forest), classification (malicious vs benign flows), clustering for unknown patterns.
- Carefully curate labeled datasets or use unsupervised methods; beware of concept drift.

## 6. Practical project ideas
- Build a passive flow-based anomaly detector using scikit-learn on NetFlow/sFlow export.
- Implement a packet sniffer that extracts TLS ServerHello cipher suites and plots common ciphers in your environment.
- Automate baseline checks for secure TLS configs across your services (scan endpoints and report weak ciphers).

## 7. Install notes
- Use virtualenv/venv.
- scapy may require additional system packages & running with elevated privileges.
- pyshark requires tshark installed on the system.

---

If you'd like, I can add step-by-step lab notebooks for any of the above projects (packet capture lab, small scanner, ML pipeline).