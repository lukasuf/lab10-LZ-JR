# https://github.com/lukasuf/lab10-LZ-JR/
# Partner 1: Lukas Zhukauskas
# Partner 2: Jose Resendiz

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(3,5), 8)
        self.assertEqual(add(10,2), 12)
    def test_subtract(self):# 3 assertions
        self.assertEqual(subtract(10,2),8)
        self.assertEqual(subtract(8,6),2)
        self.assertEqual(subtract(5,1), 4)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,3), 15)
        self.assertAlmostEqual(mul(5.5,2.25), 12.375)
        self.assertEqual(mul(-2, 5), -10)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 1), 1/5)
        self.assertAlmostEqual(div(-3, 1), -1/3)
        self.assertEqual(div(10, 0), 0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
              div(0, 5)
     # fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10,1000),3)
        self.assertEqual(logarithm(10,100), 2)
        self.assertEqual(logarithm(2,8),3)

    def test_log_invalid_base(self):# 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,4)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(5,3), 5.830951894845301)
        self.assertAlmostEqual(hypotenuse(10, 5), 11.180339887498949)
        self.assertAlmostEqual(hypotenuse(-7, 5), 8.602325267042627)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
    #     # Test basic function
        self.assertEqual(square_root(0),0)
        self.assertEqual(square_root(9),3)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
