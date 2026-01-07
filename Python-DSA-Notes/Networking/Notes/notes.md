# Networking Notes — Basic → Advanced (Security-Focused)

## 1. Big picture
- Models: OSI (7 layers) vs TCP/IP (4 layers). Understand how each layer maps to real protocols and devices.
- Core concepts: addressing (MAC, IP), routing, switching, segmentation, MTU, fragmentation, ports, stateful vs stateless services.

## 2. Key protocols (what they do, where they live, quick notes)
- Ethernet (L2): framing, MAC addresses, collisions, VLANs (802.1Q).
- ARP (L2/L3 boundary): IP→MAC resolution; ARP spoofing is an attack vector.
- IP (L3): IPv4/IPv6, routing, fragmentation, TTL, addressing schemes.
- ICMP: control messages (ping, destination unreachable).
- TCP (L4): reliable byte stream, handshake (SYN/SYN-ACK/ACK), flow & congestion control, retransmissions.
- UDP (L4): connectionless datagrams, used for DNS, video, VoIP, lighter-weight protocols.
- DNS (App): name resolution; caching, recursive vs iterative queries; DNSSEC for integrity.
- HTTP/HTTPS (App): web protocols; HTTPS = HTTP over TLS (security: TLS certificates, CAs).
- TLS: encryption, handshake, certificate chain, session resumption, cipher suites.
- SSH: secure remote shell; key-based auth, forwarding.
- SMTP/IMAP/POP (mail): legacy protocols, often augmented with TLS.
- FTP/SFTP: file transfer; SFTP (SSH) is secure; FTP is plain text.
- BGP (Inter-domain routing): path vector; critical infrastructure—BGP hijacking impact.
- OSPF, EIGRP (Interior routing): link-state/distance vector.
- DHCP: dynamic IP config; DHCP spoofing risks.
- SNMP: network management; SNMPv1/v2 insecure (plaintext), SNMPv3 has security.
- NAT / PAT: address translation; impacts end-to-end model, breaks inbound connections.
- VPN protocols: IPsec, OpenVPN, WireGuard.

## 3. Security concepts & common attacks
- Threats: DoS/DDoS, MITM, ARP poisoning, DNS spoofing, IP spoofing, SYN flood, amplification attacks, routing attacks (BGP hijack), lateral movement.
- Vulnerabilities & misconfigurations: open ports, weak TLS configs, default creds, unpatched devices, weak segmentation.
- Defensive controls: segmentation, least privilege, network access control (802.1X), IDS/IPS, WAFs, rate limiting, black/whitelisting, secure management plane.
- Detection: signature-based IDS (Snort/Suricata), anomaly detection, flow monitoring (NetFlow/sFlow/IPFIX), honeypots.
- PKI & TLS: CA model, certificate transparency, pinning, revocation (CRL/OCSP).

## 4. Observability & tools
- Packet capture: tcpdump, tshark/Wireshark — read packets, filters, follow TCP streams.
- Flow tools: nfdump, ntop, sFlow collectors.
- Scanning/Discovery: Nmap (service + version detection), masscan, ARP scanning.
- Logging/Telemetry: syslog, netflow, SNMP traps; SIEM for correlation (Splunk/ELK/QRadar).

## 5. Protocol internals & deep dives (examples)
- TCP handshake & teardown: understand sequence/ack numbers and flags, how SYN cookies mitigate SYN flood.
- TLS handshake (1.2 vs 1.3): key exchange (RSA, ECDHE), cipher suites, forward secrecy, PSK/0-RTT considerations.
- DNS: query/response formats, recursion, cache poisoning prevention (DNSSEC, 0x20 bit randomization, source port randomization).

## 6. Secure architecture patterns
- Zero Trust: assume no implicit trust, verify explicitly, microsegmentation.
- Defense in depth: layered controls (perimeter + internal + host + app).
- Secure remote access: MFA, bastion hosts, jump boxes, just-in-time access.

## 7. Practical learning path & exercises
1. Basics: subnetting, TCP/IP, read Wireshark traces for simple HTTP and DNS flows.
2. Intermediate: set up a small lab (virtual network) to test ARP spoofing, packet capture, and DNS behavior.
3. Advanced: implement an IDS rule in Suricata, analyze logs in ELK, practice secure TLS config and benchmarking.

## 8. References & further reading
- RFCs (RFC 791, RFC 793, RFC 5321, RFC 1034/1035, etc.)
- Wireshark University, MIT OpenCourseWare networking lectures, OWASP Top 10 (app security), SANS papers.

---

**Note:** This document is a starting point; networking + security is broad — pick the sub-topic you want deeper notes on and I can expand with diagrams and labs.