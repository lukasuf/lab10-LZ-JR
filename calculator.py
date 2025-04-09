# https://github.com/lukasuf/lab10-LZ-JR/
# Partner 1: Lukas Zhukauskas
# Partner 2: Jose Resendiz

import math

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
