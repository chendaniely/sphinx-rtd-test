""" Test module and some documentation
"""


def my_square(x):
    """Square a given value

    :param x: value to be squared
    :type x: a number
    :rtype: float
    """
    return x ** 2

def my_square_alternative_doc(x):
    """Square a given value

    Parameters
    ----------
    x : number
        The number you want to square

    
    Returns
    -------
    x **2 : number
        The square of the value

    Examples
    --------
    >>> my_square_alternative_doc(2)
    >>> 4
    """
    return x ** 2
