import unittest
from dns_proxy.tls_connection import create_tls_connection

class TestTLSConnection(unittest.TestCase):
    def test_create_tls_connection(self):
        conn = create_tls_connection('1.1.1.1', 853)
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == '__main__':
    unittest.main()
