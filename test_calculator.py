import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    # Test dodawania
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # Test odejmowania
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    # Test mnożenia
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 100), 0)

    # Test dzielenia
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)

        # Test dzielenia przez zero
        with self.assertRaises(ValueError):
            divide(5, 0)

    # Test dzielenia z liczbą zmiennoprzecinkową
    def test_divide_float(self):
        self.assertAlmostEqual(divide(7, 3), 2.3333333333333335, places=7)

    # Test dodawania liczb ujemnych
    def test_add_negative(self):
        self.assertEqual(add(-5, -3), -8)

    # Test odejmowania liczb zmiennoprzecinkowych
    def test_subtract_float(self):
        self.assertEqual(subtract(10.5, 4.2), 6.3)

    # Test mnożenia przez zero
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 99), 0)

    # Test dużych liczb
    def test_large_numbers(self):
        self.assertEqual(add(10**6, 10**6), 2000000)
        self.assertEqual(multiply(10**6, 10**6), 1000000000000)

if __name__ == "__main__":
    unittest.main()