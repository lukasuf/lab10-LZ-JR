# https://github.com/lukasuf/lab10-LZ-JR/
# Partner 1: Lukas Zhukauskas
# Partner 2: Jose Resendiz

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError

def hypotenuse(a,b):
    return math.hypot(a, b)

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def mul(a,b):
    return a*b
    
def div(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return b/a

def exp(a,b):
    return a**b

def logarithm(a,b):
    if a < 0 or b < 0:
        raise ValueError
    return math.log(b, a)
