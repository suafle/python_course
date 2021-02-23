"""
A collection of simple math operations
"""

def simple_add(a,b):
    """The sum of two numbers.
    
    Parameters
    ----------
    a,b : float
                
    Returns
    -------
    a+b
    """
    return a+b

def simple_sub(a,b):
    """The substraction of two numbers.
    
    Parameters
    ----------
    a,b : float
                
    Returns
    -------
    a-b
    """
    return a-b

def simple_mult(a,b):
    """The multiplication of two numbers.
    
    Parameters
    ----------
    a,b : float
                
    Returns
    -------
    a*b
    """
    return a*b

def simple_div(a,b):
    """The division of two numbers.
    
    Parameters
    ----------
    a,b : float
                
    Returns
    -------
    a/b
    """
    return a/b

def mod(a,b):
    """The remainder of the divsion.
    
    
    Parameters
    ----------
    a,b : float
                
    Returns
    -------
    a%b
    """
    return a%b

def poly_first(x, a0, a1):
    """First order polynomial.
    
    Parameters
    ----------
    x,a0,a1 : float
                
    Returns
    -------
    a1*x + a0
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Second order polynomial.
    
    Parameters
    ----------
    x,a0,a1,a2 : float
                
    Returns
    -------
    a2*x**2 + a1*x + a0
    """
    return poly_first(x, a0, a1) + a2*(x**2)
