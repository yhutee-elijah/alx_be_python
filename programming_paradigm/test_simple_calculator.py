import unittest
from programming_paradigm.simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
      """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
            """Test the addition method."""
            self.assertEqual(self.calc.add(2, 3), 5)
            self.assertEqual(self.calc.add(-1, 1), 0)
            self.assertEqual(self.calc.add(0, 0), 0)
            self.assertEqual(self.calc.add(-5, -3), -8)
            self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
            self.assertEqual(self.calc.add(-1.5,-2.5), 4.0)
            self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
            self.assertEqual(self.calc.add(-1e10, -1e10), -2e10)
            self.assertEqual(self.calc.add(1e-10, 1e-10), 2e-10)
            self.assertEqual(self.calc.add(-1e-10, -1e-10), -2e-10)

    def test_subtraction(self):
      """Test the subtraction method."""
      
      self.assertEqual(self.calc.subtract(1, 1), 0)
      self.assertEqual(self.calc.subtract(-1, -1), 0)
      self.assertEqual(self.calc.subtract(0, 0), 0)
      self.assertEqual(self.calc.subtract(5, 3), 2)
      self.assertEqual(self.calc.subtract(-5, -3), -2)
      self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)
      self.assertEqual(self.calc.subtract(-1.5, -0.5), -1.0)
      self.assertEqual(self.calc.subtract(1e10, 1e10), 0)
      self.assertEqual(self.calc.subtract(-1e10, -1e10), 0)
      self.assertEqual(self.calc.subtract(1e-10, 1e-10), 0)
      self.assertEqual(self.calc.subtract(-1e-10, -1e-10), 0)
      self.assertEqual(self.calc.subtract(1e10, 1e-10), 1e10)
      self.assertEqual(self.calc.subtract(-1e10, 1e-10), -1e10)
      self.assertEqual(self.calc.subtract(1e-10, 1e10), -1e10)
      self.assertEqual(self.calc.subtract(-1e-10, 1e10), -1e10)

    def test_multiplication(self):
      """Test the multiplication method"""
      self.assertEqual(self.calc.multiply(1, 1), 1)
      self.assertEqual(self.calc.multiply(0, 1), 0)
      self.assertEqual(self.calc.multiply(-1, 1), -1)
      self.assertEqual(self.calc.multiply(1.5, 2), 3.0)
      self.assertEqual(self.calc.multiply(-1.5, -2), 3.0)
      self.assertEqual(self.calc.multiply(1e10, 1e10), 1e20)
      self.assertEqual(self.calc.multiply(-1e10, -1e10), 1e20)
      self.assertEqual(self.calc.multiply(1e-10, 1e10), 1.0)
      self.assertEqual(self.calc.multiply(-1e-10, 1e10), -1.0)
      self.assertEqual(self.calc.multiply(1e10, 1e-10), 1.0)
      self.assertEqual(self.calc.multiply(-1e10, 1e-10), -1.0)

    def test_division(self):
      self.assertEqual(self.calc.divide(1, 1), 1)
      self.assertEqual(self.calc.divide(-1, 1), -1)
      self.assertEqual(self.calc.divide(1, -1), -1)
      self.assertEqual(self.calc.divide(-1, -1), 1)
      self.assertEqual(self.calc.divide(1.5, 0.5), 3.0)
      self.assertEqual(self.calc.divide(-1.5, -0.5), 3.0)
      self.assertEqual(self.calc.divide(1e10, 1e10), 1.0)
      self.assertEqual(self.calc.divide(-1e10, -1e10), 1.0)
      self.assertEqual(self.calc.divide(1e-10, 1e-10), 1.0)
      self.assertEqual(self.calc.divide(-1e-10, -1e-10), 1.0)
      self.assertEqual(self.calc.divide(1e10, 1e-10), 1e20)
      self.assertEqual(self.calc.divide(-1e10, 1e-10), -1e20)
      self.assertEqual(self.calc.divide(1e-10, 1e10), 1e-20)
      self.assertEqual(self.calc.divide(-1e-10, 1e10), -1e-20)
      with self.assertRaises(ZeroDivisionError):
          self.calc.division(1, 0)
      with self.assertRaises(ZeroDivisionError):
          self.calc.division(-1, 0)
      with self.assertRaises(ZeroDivisionError):
          self.calc.division(0, 0)
                        
        if __name__ == "__main__":
            unittest.main(verbosity=2)
