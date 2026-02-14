import unittest
from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(5, 3), 2)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(1, 2, 3), 6)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator.fun2("a", 3)


if __name__ == "__main__":
    unittest.main()
