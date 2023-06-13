from basics import multiplyNumbers
import unittest

print("product:", multiplyNumbers(4, 5, 6, 56))

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = multiplyNumbers(4, 5, 6, 56)
        self.assertEqual(calculation, 6720, 'The sum is wrong.')

if __name__ == '__main__':
    unittest.main()

