import math
from pytest import approx


def cels_from_fahr(fahr):
    """Convert a temperature i Fahrenhit to Celsius and retures
    teh Celsius temprearature"""

    cels = (fahr - 32) * 5 / 9
    return cels