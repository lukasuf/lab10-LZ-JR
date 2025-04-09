"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a/b
def log(a,b):
    if a<=0 or b<=0:
        raise ValueError("Incorrect input for log")
    else:
        return math.log(b,a)
def exp(a,b):
    return a**b
