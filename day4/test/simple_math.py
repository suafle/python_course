"""
A collection of simple math operations
"""

def simple_add(a,b):
    """The sum of two numbers.
    """
    return a+b

def simple_sub(a,b):
    """The substraction of two numbers.
    """
    return a-b

def simple_mult(a,b):
    """The multiplication of two numbers.
    """
    return a*b

def simple_div(a,b):
    """The division of two numbers.
    """
    return a/b

def mod(a,b):
    """The remainder of the divsion.
    """
    return a%b

def poly_first(x, a0, a1):
    """First order polynomial.
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Second order polynomial.
    """
    return poly_first(x, a0, a1) + a2*(x**2)
