#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
# UFRJ - PPGI
# MAB719
# Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 2.1
"""

import thinkstats
import math
    
_pumpkins_weight = [1, 1, 1, 3, 3, 591]

def Pumpkin(pumpkins_weight):
    """
    Calculate the mean and 
    """
    mu, var = thinkstats.MeanVar(pumpkins_weight)
    return mu, var, math.sqrt(var)

if __name__ == '__main__':

    print Pumpkin(_pumpkins_weight)
