# https://github.com/lukasuf/lab10-LZ-JR/
# Partner 1: Lukas Zhukauskas
# Partner 2: Jose Resendiz

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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