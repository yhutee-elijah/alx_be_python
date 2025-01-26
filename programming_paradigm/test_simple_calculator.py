import unittest
from programming_paradigm.simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(1, 2), 3)

    def test_subtract(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(2, 1), 1)

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

    def test_divide(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(6, 3), 2)

        def test_edge_case(self):
                calc = SimpleCalculator()
                self.assertIsNone(calc.divide(6, 0))
                        
        if __name__ == "__main__":
            unittest.main()