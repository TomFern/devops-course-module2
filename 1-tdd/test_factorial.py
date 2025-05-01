import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    # example TDD test
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)
    # write a few more tests....


if __name__ == '__main__':
    unittest.main()
