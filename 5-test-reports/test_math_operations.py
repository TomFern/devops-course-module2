import unittest

# Sample arithmetic functions for testing
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is undefined")
    return a / b

class TestMathOperations(unittest.TestCase):
    
    def test_addition_positive(self):
        # Expected to pass: 2 + 3 = 5
        self.assertEqual(add(2, 3), 5)

    def test_addition_negative(self):
        # Expected to pass: (-1) + (-1) = -2
        self.assertEqual(add(-1, -1), -2)

    def test_addition_fail(self):
        # Intentionally failing: 2 + 3 should be 5, not 6
        self.assertEqual(add(2, 3), 6)

    def test_subtraction(self):
        # Expected to pass: 10 - 5 = 5
        self.assertEqual(subtract(10, 5), 5)

    def test_subtraction_fail(self):
        # Intentionally failing: 10 - 5 should be 5, not 4
        self.assertEqual(subtract(10, 5), 4)

    def test_multiplication(self):
        # Expected to pass: 3 * 4 = 12
        self.assertEqual(multiply(3, 4), 12)

    def test_multiplication_fail(self):
        # Intentionally failing: 3 * 4 should be 12, not 11
        self.assertEqual(multiply(3, 4), 11)

    def test_division(self):
        # Expected to pass: 10 / 2 = 5
        self.assertEqual(divide(10, 2), 5)

    def test_division_exception(self):
        # Expected to pass: division by zero raises an exception
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_division_fail(self):
        # Intentionally failing: 10 / 3 is approximately 3.33,
        # but we use a wrong expectation to force a failure.
        self.assertAlmostEqual(divide(10, 3), 3.33, places=2)

    def test_complex_operation(self):
        # Expected to pass:
        # (2*3) + (10 - (20/4)) = 6 + (10 - 5) = 11
        result = add(multiply(2, 3), subtract(10, divide(20, 4)))
        self.assertEqual(result, 11)

    def test_complex_operation_fail(self):
        # Intentionally failing: expecting the result to be 12 instead of 11
        result = add(multiply(2, 3), subtract(10, divide(20, 4)))
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()

