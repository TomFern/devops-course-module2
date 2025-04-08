import unittest
import requests

class TestEndToEnd(unittest.TestCase):
    def test_home_page(self):
        response = requests.get("http://127.0.0.1:5000/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome", response.text)

    def test_add_endpoint(self):
        payload = {"a": 5, "b": 7}
        response = requests.post("http://127.0.0.1:5000/add", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["result"], 12)

if __name__ == '__main__':
    unittest.main()
