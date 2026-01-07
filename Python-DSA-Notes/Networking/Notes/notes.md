# Networking Notes — Basic → Advanced (Security-Focused)

## 1. Big picture
- Models: OSI (7 layers) vs TCP/IP (4 layers). Understand how each layer maps to real protocols and devices.
- Core concepts: addressing (MAC, IP), routing, switching, segmentation, MTU, fragmentation, ports, stateful vs stateless services.

## 2. Key protocols (what they do, where they live, quick notes)

### Ethernet (Layer 2) — how it works, practical use, and testing 🔎
- What it is: The dominant LAN technology defining frame formats, MAC addressing, and how switches forward frames.
- Frame structure: preamble/SFD, destination MAC, source MAC, EtherType/length, payload, FCS (CRC).
- How switching works: switches learn source MAC→port mappings, forward frames by destination MAC, and flood unknown destinations to all ports. Modern switches support full-duplex links and no CSMA/CD on switched links.
- VLANs (802.1Q): tag frames to create separate broadcast domains on the same physical network. VLAN tags add fields inside the Ethernet frame.
- MTU & fragmentation: Typical Ethernet MTU = 1500 bytes; fragmentation occurs at higher layers (IP) when payload exceeds MTU.

Practical uses:
- LAN connectivity (servers, workstations, access points) and data-center fabric.
- Use VLANs for segmentation, QoS for prioritization, and link aggregation for higher throughput.

Inspection & tools:
- Wireshark filters: `eth.addr == <mac>`, `eth.type == 0x8100` (802.1Q), `frame.len`.
- Scapy example (viewing/creating L2 frames) — valuable for learning and safe experiments on a lab network.

Security considerations:
- MAC spoofing and VLAN hopping are common L2 attack techniques.
- Mitigations: port-security, BPDU guard, private VLANs, and strict VLAN boundary enforcement.

Lab idea:
- Put two VMs on the same host-only network, capture traffic with Wireshark, craft an 802.1Q-tagged frame with Scapy, and observe how the switch/host reacts.

---

### ARP (Address Resolution Protocol) — L2/L3 boundary 🔗
- How it works: ARP maps IPv4 addresses to MAC addresses in the local LAN. A host broadcasts an ARP request "Who has <IP>?" and the owner replies with an ARP response containing its MAC.
- Practical uses: Required for local delivery of IPv4 packets on Ethernet. ARP caches store recently-resolved mappings.
- Inspection & tools: Wireshark filter `arp`; check ARP table (`arp -a` on Windows, `ip neigh` or `arp` on Linux). Use Scapy to craft ARP requests/responses.

Security considerations:
- ARP spoofing/poisoning: an attacker responds with fake IP→MAC mappings to perform MITM, traffic interception or DoS.
- Mitigations: static ARP entries for critical hosts, Dynamic ARP Inspection (on switches), port-security, monitoring for sudden changes to ARP tables.

Safe lab idea:
- In an isolated VM lab, capture normal ARP requests, then craft a benign ARP reply for a test IP with Scapy and observe effects (do NOT perform ARP poisoning on live networks).

Scapy example (harmless ARP request watcher):
```python
from scapy.all import sniff, ARP

def show(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 1:  # who-has
        print(f"ARP request: {pkt[ARP].psrc} -> {pkt[ARP].pdst}")

sniff(filter='arp', prn=show, count=0)
```

---

### IP (IPv4 / IPv6) — Layer 3 fundamentals 🌐
- How it works: IP provides addressing and routing. IPv4 uses 32-bit addresses, IPv6 uses 128-bit. Routers use routing tables and protocols to forward packets between networks.
- Key concepts: subnetting, CIDR notation, default gateway, TTL/hop limit, fragmentation (IPv4), path MTU discovery.
- Inspection & tools: `ip addr`, `ip route`, `ping`, `traceroute`/`tracert`, Wireshark filters `ip`, `ipv6`.

Security considerations:
- IP spoofing, misconfigured subnets, and weak routing policies can enable attacks and traffic leakage.
- Best practices: apply ACLs, implement anti-spoofing (uRPF), use segmentation and firewalling.

Lab idea:
- Practice subnetting exercises; set up an example network and verify routing tables. Capture fragmented packets and reassembly behavior in Wireshark.

---

### ICMP (Internet Control Message Protocol) — diagnostics & control 🛠️
- How it works: ICMP sends control messages (echo request/reply, destination unreachable, time exceeded). Often used by `ping` and `traceroute`.
- Inspection & tools: `ping`, `traceroute`, Wireshark filter `icmp`.

Security considerations:
- ICMP can be abused for reconnaissance (ping sweeps) or as part of amplification/DoS; some networks limit ICMP types.
- Mitigations: rate-limit ICMP, allow essential types only, inspect unusual ICMP payloads.

Lab idea:
- Use Wireshark to observe `ping` and `traceroute` flows and analyze TTL decrementing and ICMP Time Exceeded messages.

---

### TCP (Transmission Control Protocol) — reliable transport 📦
- How it works: TCP is a connection-oriented protocol providing ordered, reliable byte streams using sequence and acknowledgment numbers, three-way handshake (SYN, SYN-ACK, ACK), flow and congestion control, and connection teardown (FIN/ACK).
- Inspection & tools: Wireshark `tcp` filter, follow TCP stream, examine flags and sequence/ack numbers.

Security considerations:
- SYN flood attacks (DoS), session hijacking, TCP reset attacks, and abuse via misconfigured services.
- Mitigations: SYN cookies, rate-limiting, proper timeout tuning, and application-layer protections.

Practical labs & tips:
- Capture a TCP handshake in Wireshark, inspect SYN, SYN-ACK, ACK and the sequence/ack increments.
- Observe retransmissions and ACK behavior by inducing artificial loss in a lab.

---

### UDP (User Datagram Protocol) — lightweight transport ⚡
- How it works: UDP provides connectionless, best-effort datagrams with no ordering or reliability guarantees; low-latency apps (DNS, VoIP) commonly use it.
- Inspection & tools: Wireshark `udp` filter; check DNS over UDP with `dig`.

Security considerations:
- UDP-based amplification attacks (e.g., DNS, NTP), spoofed source addresses.
- Mitigations: rate limiting, response-size controls, source validation where possible.

Lab idea:
- Send/receive UDP packets using `socat` or simple Python `socket` snippets; observe behavior when server drops packets.

---

### DNS (Domain Name System) — name resolution 🧭
- How it works: DNS resolves names to IPs using recursive/iterative queries, authoritative name servers, and zones. Important records: A/AAAA, CNAME, NS, SOA, TXT, MX.
- Inspection & tools: `dig`, `nslookup`, Wireshark `dns` filter; capture queries and responses.

Security considerations:
- Cache poisoning, DNS hijacking, and insecure recursive resolvers. DNSSEC adds integrity via signatures; DANE and DNS over TLS/HTTPS (DoT/DoH) add confidentiality.

Lab idea:
- Run a local dnsmasq or BIND instance in a VM; perform queries, simulate TTL changes and capture responses. Explore `dig +trace` and use `dnseval`/`dnssec-tools` to inspect DNSSEC.

---

### HTTP / HTTPS — web protocols & security 🌍
- How it works: HTTP is an application-layer protocol for web resources; HTTPS is HTTP over TLS. Understand requests/responses, methods (GET/POST/PUT/DELETE), status codes, cookies, and headers.
- Inspection & tools: browser dev tools, `curl -I`, Wireshark `http` or `tls` filters for HTTPS; `openssl s_client` to inspect TLS handshakes.

Security considerations:
- TLS misconfigurations, weak ciphers, missing HSTS, open redirects and insecure cookies.
- Mitigations: enforce TLS 1.2+/1.3, strong ciphers, HSTS, secure cookie flags, CSP, and proper cert management.

Lab idea:
- Use `openssl s_client -connect host:443 -servername host` to view certificate chain and cipher. Capture a TLS handshake in Wireshark and observe the ServerHello and certificate exchange.

---

### TLS (Transport Layer Security) — encryption essentials 🔐
- How it works: TLS provides confidentiality and integrity with a handshake (1.2 vs 1.3 differences), key exchange (RSA, ECDHE), and cipher suites. TLS 1.3 streamlines the handshake and mandates forward secrecy for many negotiating suites.
- Inspection & tools: `openssl`, `testssl.sh`, `sslyze`, Wireshark `tls` filter.

Security considerations:
- Use modern TLS versions, prefer ECDHE, disable RC4 and export ciphers, and watch for weak server configurations and certificate issues.

Lab idea:
- Scan an endpoint with `testssl.sh` to see supported protocols and ciphers; create a local test server with weak ciphers to show why they're dangerous.

---

### SSH — secure shell & automation 🗝️
- How it works: SSH provides secure remote login and tunneling using public-key or password-based authentication. It supports port forwarding and SFTP for file transfers.
- Inspection & tools: `ssh`, `sshd` config, `ssh-keygen`, `Paramiko`/`Netmiko` for automation.

Security considerations:
- Enforce key-based auth, disable root logins, and limit available ciphers and MACs. Monitor for suspicious login attempts and use MFA where possible.

Lab idea:
- Automate a configuration check using Paramiko that logs into a test VM and gathers `sshd_config` settings for compliance.

---

### DHCP — dynamic address assignment 🚪
- How it works: DHCP assigns IP config (address, gateway, DNS) via a broadcast discover/offers/request/ack exchange.
- Inspection & tools: Wireshark `bootp`/`dhcp`, `dhclient`/`dhcpd` logs.

Security considerations:
- Rogue DHCP servers can hand out malicious configurations. Mitigations: DHCP snooping on switches, DHCP relay configuration, static reservations for critical hosts.

Lab idea:
- Set up a lab DHCP server and observe DHCP exchange in Wireshark; simulate a misconfigured DHCP to test client behavior in a safe environment.

---

### BGP & Routing Security — inter-domain routing 🌐
- How it works: BGP is a path-vector protocol exchanging reachability between autonomous systems (AS). Routes are chosen by policy and AS-path attributes.
- Inspection & tools: `bgp` table views on routers, `bgpstream`, `looking-glass` services, RPKI validators.

Security considerations:
- BGP hijacks and leaks can divert traffic globally. RPKI/ROA adoption, prefix filtering, and BGP monitoring reduce risk.

Lab idea:
- Use a BGP simulator (e.g., Quagga/FRRouting in containers) to simulate announcements and observe route propagation and policy impacts.

---

### OSPF / EIGRP — interior routing protocols 🧭
- How they work: OSPF (link-state) uses LSAs to build a topology map; EIGRP (Cisco proprietary) uses composite metrics and diffusing updates.
- Inspection & tools: router show commands (OSPF LSDB), GNS3 or Mininet labs, debug outputs.

Security considerations:
- Authentication of routing protocol peers, route filtering, TTL security (OSPF area boundary controls), and monitoring for unexpected LSAs.

Lab idea:
- Create a small lab with FRR/Quagga or GNS3 to view OSPF LSA floods and experiment with route flaps and LSDB convergence.

---

### SNMP — network management & telemetry 📈
- How it works: SNMP (v1/v2c/v3) provides MIB-based access to device metrics. v1/v2c use community strings (plaintext), v3 adds authentication and encryption.
- Inspection & tools: `snmpwalk`, `snmpget`, SNMP managers, and Wireshark `snmp` filters.

Security considerations:
- Replace default community strings, use SNMPv3, restrict access with ACLs, and monitor for suspicious queries.

Lab idea:
- Query a test SNMP agent with `snmpwalk` and explore MIB trees; then configure SNMPv3 credentials.

---

### NAT / PAT & VPNs — translation and secure tunnels 🔁
- How NAT/PAT works: Network Address Translation rewrites IP headers to translate private ↔ public addresses (PAT multiplexes many private addresses via port translation).
- VPNs: IPsec, OpenVPN, and WireGuard provide encrypted tunnels for secure remote connectivity.
- Inspection & tools: `iptables`/`nftables` NAT rules, `ipsec` tools, `wg` for WireGuard.

Security considerations:
- NAT breaks end-to-end connectivity and can hide source addresses; VPNs must use strong crypto and correct auth.

Lab idea:
- Set up a WireGuard tunnel between two VMs, inspect encapsulated packets, and verify traffic flows through the tunnel.

---

**Note:** Each protocol section above includes practical inspection tips, security considerations, and a simple lab idea. If you'd like, I can convert selected labs into Jupyter notebooks with step-by-step instructions and packet captures.

## 3. Security concepts & common attacks
- Threats: DoS/DDoS, MITM, ARP poisoning, DNS spoofing, IP spoofing, SYN flood, amplification attacks, routing attacks (BGP hijack), lateral movement.
- Vulnerabilities & misconfigurations: open ports, weak TLS configs, default creds, unpatched devices, weak segmentation.
- Defensive controls: segmentation, least privilege, network access control (802.1X), IDS/IPS, WAFs, rate limiting, black/whitelisting, secure management plane.
- Detection: signature-based IDS (Snort/Suricata), anomaly detection, flow monitoring (NetFlow/sFlow/IPFIX), honeypots.
- PKI & TLS: CA model, certificate transparency, pinning, revocation (CRL/OCSP).
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