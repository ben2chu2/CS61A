######################
# Required Questions #
######################


def temperature_converter(f_temp):
    """
    >>> celsius_temp1 = temperature_converter(32)
    >>> celsius_temp1
    0.0
    """
    return ((f_temp - 32) * 2)/9


def pythagorean_triple(a,b,c):
    """
    >>> pythagorean_triple(3,4,5)
    True
    >>> pythagorean_triple(3,4,6)
    False
    """
    return c**2 == a**2 + b**2
