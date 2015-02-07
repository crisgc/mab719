#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
UFRJ - PPGI - NCE
MAB719
Cristiano Gurgel de Castro <crisgc1@gmail.com>

Exercicio
Implemente todas essas medidas de dispersão em python e compare com os
resultados e compare com os métodos implementados em www.thinkstats.
com/thinkstats.py
"""

import math

def mean(data):
    """ 
    Calculates the mean of a data set

    Args:
        data: the list with the data
    """

    n = len(data)
    if (n > 0) :
        result = math.fsum(data) / n
        return result

def amplitude(data):
    """ 
    Calculates the amplitude of a data list. 
    """
   
    n = len(data)
    if (n == 0) :
        amplitude = None
    else :
        min_value = min(data)
        max_value = max(data)
        amplitude = (max_value + min_value) / 2.0
    
    return amplitude

def deviation(data):
    """ Calculates the deviation of elements on a given list
    """

    # Verify if the mean was given, and if it wasn't calculate it!
    x = mean(data)

    n = len(data)
    if n != 0:
        result = [(datum - x) for datum in data]

    return result

def mean_deviation(data):
    """ Calculates the mean deviation of the elements on a given list
    """
    
    dev_values = deviation(data)
    abs_devs = [abs(dev) for dev in dev_values]
    result = math.fsum(abs_devs) / len(data)
    return result

def variation(data):
    """ Calculates the standard deviation of the elements on a given list
    """
    n = len(data)
    if (n > 1) :
        dev_values = deviation(data)
        square_values = [x**2 for x in dev_values]
        result = math.fsum(square_values)
        result /= (n-1)
        return result

def standard_deviation(data):
    """ Calculate the standard deviation
    """
    n = len(data)
    if (n > 1):
        result = math.sqrt(variation(data))
        return result

if __name__ == '__main__' :
    numbers = [ 10, 14, 18, 6, 19, 12, 11, 7, 3, 15, 9, 5, 2, 8, 20, 16, 4, 1,
            17, 13 ]
    print( numbers )
    n = mean(numbers)
    print( "Mean: %.2f" % n )
    print( "Amplitude: %.2f" % amplitude(numbers) )
    print( "Deviation:" )
    print( deviation(numbers) )
    print( "Desvio medio: %.2f" % mean_deviation(numbers) )
    print( "Variation: %.2f" % variation(numbers))
    print( "Stnd Deviation: %.2f" % standard_deviation(numbers) )
