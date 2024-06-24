import time

class DNSCache:
    def __init__(self, ttl=300):
        self.cache = {}
        self.ttl = ttl

    def get(self, query):
        if query in self.cache:
            entry = self.cache[query]
            if time.time() - entry['timestamp'] < self.ttl:
                return entry['response']
            else:
                del self.cache[query]
        return None

    def set(self, query, response):
        self.cache[query] = {
            'response': response,
            'timestamp': time.time()
        }
