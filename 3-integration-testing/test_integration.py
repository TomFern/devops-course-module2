import unittest
from service import process_and_store, retrieve_processed
from datastore import database

class TestIntegration(unittest.TestCase):
    def setUp(self):
        database.clear()  # Ensure a clean slate

    def test_process_store_and_retrieve(self):
        key = "greeting"
        raw_value = "  Hello World  "
        processed = process_and_store(key, raw_value)
        self.assertEqual(processed, "HELLO WORLD")
        retrieved = retrieve_processed(key)
        self.assertEqual(retrieved, "hello world")

if __name__ == '__main__':
    unittest.main()
