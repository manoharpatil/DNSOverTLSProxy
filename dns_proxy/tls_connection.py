import socket
import ssl
from dns_proxy.config import Config

config = Config()

def create_tls_connection(dns_over_tls_server, dns_over_tls_port):
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=dns_over_tls_server,
    )
    conn.connect((dns_over_tls_server, dns_over_tls_port))
    return conn
