# Use a lightweight Python image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the DNS proxy code into the container
COPY dns_proxy/ dns_proxy/
COPY dns_proxy/main.py main.py

# Run the DNS proxy
CMD ["python", "main.py"]
