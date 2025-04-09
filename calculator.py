# https://github.com/lukasuf/lab10-LZ-JR/
# Partner 1: Lukas Zhukauskas
# Partner 2: Jose Resendiz

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a, b)

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a,b):
    return math.log(b, a)

def exponent(a,b):
    return a**b