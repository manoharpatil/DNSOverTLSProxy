import socket
import threading
import logging
from dns_proxy.tls_connection import create_tls_connection
from dns_proxy.cache import DNSCache
from dns_proxy.config import Config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dns_cache = DNSCache()
config = Config()

def handle_dns_query(client_socket, client_address, is_udp=False):
    try:
        query, addr = client_socket.recvfrom(512) if is_udp else (client_socket.recv(512), client_address)
        logger.info(f"Received query from {client_address}: {query}")

        cached_response = dns_cache.get(query)
        if cached_response:
            logger.info(f"Cache hit for query: {query}")
            response = cached_response
        else:
            conn = create_tls_connection(config.dns_over_tls_server, config.dns_over_tls_port)
            conn.send(query)  # Forward the query to the DNS-over-TLS server
            response = conn.recv(512)  # Get the response
            logger.info(f"Received response from DNS-over-TLS server: {response}")
            dns_cache.set(query, response)

        client_socket.sendto(response, addr) if is_udp else client_socket.send(response)  # Send the response back to the client
    except Exception as e:
        logger.error(f"Error handling query from {client_address}: {e}")
    finally:
        client_socket.close()
        if not cached_response:
            conn.close()

def start_tcp_proxy():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 53))  # Listen on port 53 for DNS queries
    server_socket.listen(5)
    logger.info("TCP DNS proxy listening on port 53...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_dns_query, args=(client_socket, client_address))
        client_handler.start()

def start_udp_proxy():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 53))  # Listen on port 53 for DNS queries
    logger.info("UDP DNS proxy listening on port 53...")

    while True:
        client_socket, client_address = server_socket.recvfrom(512)
        client_handler = threading.Thread(target=handle_dns_query, args=(server_socket, client_address, True))
        client_handler.start()

if __name__ == '__main__':
    threading.Thread(target=start_tcp_proxy).start()
    threading.Thread(target=start_udp_proxy).start()
