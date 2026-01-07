"""Simple HTTP probe to show headers and TLS info."""
import requests


def probe(url, timeout=5):
    try:
        r = requests.get(url, timeout=timeout)
        return r.status_code, r.headers
    except Exception as e:
        return None, str(e)


if __name__ == '__main__':
    url = 'https://example.com'
    status, hdrs = probe(url)
    print('status:', status)
    print('server header:', hdrs.get('Server') if isinstance(hdrs, dict) else hdrs)
