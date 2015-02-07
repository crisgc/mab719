#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
UFRJ - PPGI
MAB719
Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 2.3
"""

import operator
import Pmf
import logging

def Mode(h):
    """
    Calculates the mode of a Histogram

    Args:
        h: the histogram
    """

    items = h.Items()

    logging.info("Lista")
    logging.info(items)
    (key , value) = max( items , key=(lambda (x,y): y))

    logging.info(key)
    result = key

    return result
        

def AllModes(h):
    """
    Return the modes of the items in descending order
    """
    result = sorted( h.Items() , key = operator.itemgetter(1) , reverse =
            True)
    return result

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    numbers = [ 10, 14, 18, 6, 19, 12, 11, 7, 3, 15, 9, 5, 2, 8, 20, 16, 4, 1,
            17, 13 , 14 ]

    h = Pmf.MakeHistFromList(numbers)
    print "Mode: %d" % Mode(h)
    print "All Modes:", AllModes(h)
