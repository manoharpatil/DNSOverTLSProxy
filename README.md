# DNS to DNS-over-TLS Proxy

## Overview
This project implements a DNS to DNS-over-TLS proxy that enhances privacy by encrypting DNS queries. The proxy listens for conventional DNS queries and forwards them to a DNS-over-TLS server (e.g., Cloudflare).

## Requirements
- Python 3.9+
- Docker

## Project Structure
```

DNSOverTLSProxy/
├── .idea/                     # IntelliJ IDEA project files
├── dns_proxy/
│   ├── __init__.py
│   ├── main.py                # Main application code
│   ├── tls_connection.py      # TLS connection logic
|   ├── cache.py               # Cache implementation
│   ├── config.py              # Configuration file
│   └── utils.py               # Utility functions
├── Dockerfile                 # Dockerfile for containerizing the application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── tests/
│   ├── __init__.py
│   ├── test_main.py           # Tests for main application logic
│   └── test_tls_connection.py # Tests for TLS connection logic
└── .gitignore                 # Git ignore file

```

## Setup and Running
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. **Build the Docker Image**:
   ```bash
   docker build -t dns-proxy .

3. **Run the Docker container**:
   ```bash
   docker run -p 53:53 -e DNS_OVER_TLS_SERVER=1.1.1.1 -e DNS_OVER_TLS_PORT=853 dns-proxy

## Security Concerns
- Ensure the proxy server is not open to the internet without proper security measures (e.g., firewall rules).
- Implement logging and monitoring to detect and prevent abuse.

## Integration
- Deploy the proxy within a containerized microservices architecture.
- Use Kubernetes or similar orchestration tools for managing and scaling the proxy instances.

## Improvements
- Handle multiple incoming requests simultaneously.
- Add support for UDP queries.
- Implement caching for improved performance.
- Enhance logging and error handling.
- Make the DNS-over-TLS server configurable.

## How to Run and Test
- Running the Project in IntelliJ or PyCharm IDEA
1. **Open the Project**:
   ```bash
   Open IntelliJ or PyCharm IDEA and navigate to `File > Open` and select the `DNSOverTLSProxy` directory.

2. **Configure Python Interpreter**:
   ```bash
   IntelliJ
   Go to `File > Project Structure > Project > Project SDK` and select your Python interpreter.
   
   PyCharm
   Go to `File > Settings > Project: DNSOverTLSProxy > Python Interpreter` and select your Python interpreter. If you don't have one set up, you can add a new interpreter by clicking on the gear icon and selecting "Add".

3. **Run the Application**:
   ```bash
   Open `dns_proxy/main.py` and click the `Run` button in IntelliJ IDEA.

4. **Build and Run Docker Container**:
   ```bash
   Open the terminal in IntelliJ IDEA.
   Build the Docker image: `docker build -t dns-proxy .`
   Run the Docker container: `docker run -p 53:53 -e DNS_OVER_TLS_SERVER=1.1.1.1 -e DNS_OVER_TLS_PORT=853 dns-proxy`
   
### Configure Your System to Use the Local DNS Proxy
- To test the DNS proxy, you need to configure your system to use localhost as the DNS server.
1. **On Windows**:
   ```
   1. Open "Control Panel". 
   2. Go to "Network and Sharing Center".
   3. Click on "Change adapter settings".
   4. Right-click on your active network connection and select "Properties".
   5. Select "Internet Protocol Version 4 (TCP/IPv4)" and click "Properties".
   6. Select "Use the following DNS server addresses".
   7. Set the "Preferred DNS server" to `127.0.0.1`.
   8. Click "OK" to apply the changes.
   ```
   
2. **On macOS**:
   ```
   1. Open "System Preferences".
   2. Go to "Network".
   3. Select your active network connection and click "Advanced".
   4. Go to the "DNS" tab.
   5. Click the "+" button and add 127.0.0.1 to the list of DNS servers.
   6. Click "OK" and then "Apply".
   ```

3. **On Linux**:
   ```
   1. Open a terminal.
   2. Edit the `/etc/resolv.conf` file with your preferred text editor (you might need superuser permissions):
      sudo nano /etc/resolv.conf
   3. Add the following line at the top of the file:
      nameserver 127.0.0.1
   4. Save and close the file.
   ```
   
### Test the DNS Proxy
1. **Test using `dig` or `nslookup`**:
   ```
   Open a terminal and use the `dig` or `nslookup` command to test DNS resolution through the proxy.
   dig example.com
   
   or
   
   nslookup example.com

   You should see the DNS resolution result. If the proxy is working correctly, the query will be forwarded to the DNS-over-TLS server and the response will be returned.
   ```
   
2. **Check Logs**:
   ```
   Please check logs of dns_proxy/main.py file to monitor the incoming requests and outgoing responses. 
   We can add simple print statements in the handle_dns_query function to log the queries and responses.
   ```
   
3. **Browser Test**:
   ```
   Open a web browser and try to access a website. If the DNS proxy is working correctly, the DNS resolution should be 
   handled by your proxy, and you should be able to browse the web normally.
   ```

4. **Revert DNS Settings**:
   ```
   After testing, don't forget to revert your DNS settings back to their original state to avoid any disruptions in your 
   network connectivity.
   ```

## Resources
- Cloudflare DNS-over-TLS: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/
- RFC 7858: https://datatracker.ietf.org/doc/html/rfc7858
