# src/test/test_assignment_3.py
import unittest
import sys
import os

# Add main directory to Python path for correct import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from assignment_3 import euler_method, runge_kutta_method

class TestNumericalMethods(unittest.TestCase):

    def setUp(self):
        self.f = lambda t, y: t - y**2
        self.a, self.b, self.N, self.y0 = 0, 2, 10, 1

    def test_euler_method(self):
        result = euler_method(self.f, self.a, self.b, self.N, self.y0)
        expected = 1.2446380979332121
        self.assertAlmostEqual(result, expected, places=4)

    def test_runge_kutta_method(self):
        result = runge_kutta_method(self.f, self.a, self.b, self.N, self.y0)
        expected = 1.251316587879806
        self.assertAlmostEqual(result, expected, places=5)

if __name__ == "__main__":
    # Adjust the path to import from main
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))
    unittest.main()
