import unittest
from math_sum import add

class TestMathUtils(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    # implement more tests


if __name__ == '__main__':
    unittest.main()
