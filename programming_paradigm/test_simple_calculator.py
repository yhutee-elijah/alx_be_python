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

        def test_edge_case(self):
                calc = SimpleCalculator()
                self.assertIsNone(calc.divide(6, 0))
                        
        if __name__ == "__main__":
            unittest.main()
