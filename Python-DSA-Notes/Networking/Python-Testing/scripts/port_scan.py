"""Simple and ethical TCP port probe. Use only on authorized targets."""
import socket


def probe(host, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except Exception:
            return False


if __name__ == '__main__':
    host = 'scanme.nmap.org'  # example public host intended for scanning practice
    ports = [22, 80, 443, 3306]
    for p in ports:
        print(p, 'open' if probe(host, p) else 'closed')
