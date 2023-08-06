import numpy as np

def multiply(number, multiplier):
    """

    :param number: The number to multiply
    :Type: float

    :param multiplier: The multiplier
    :Type: float
    :return: float
    """
    return number * multiplier

class Multiplication:
    """
    Instantiate a multiplication operation
    Blablaabla
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        """
        lablbalbalbalbabla
        :param number:
        :return:
        """
        return np.dot(number, self.multiplier)