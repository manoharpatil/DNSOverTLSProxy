import os

class Config:
    def __init__(self):
        self.dns_over_tls_server = os.getenv('DNS_OVER_TLS_SERVER', '1.1.1.1')  # Default to Cloudflare
        self.dns_over_tls_port = int(os.getenv('DNS_OVER_TLS_PORT', 853))
