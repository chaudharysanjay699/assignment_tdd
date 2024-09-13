import re

class Calculator:

    def add(self, str_numbers: str):
        if not str_numbers:
            return 0
        #Find the all required value here
        numbers = list(map(int,re.findall(r'[+-]?\d+\.?\d*', str_numbers)))
        
        # find the negative values if any
        negatives = [num for num in numbers if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")


        return sum(numbers)

# Unit Tests

import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)

    def test_newline_as_special_char(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_special_char(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2, -3")

if __name__ == '__main__':
    unittest.main()
