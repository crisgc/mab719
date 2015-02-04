#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
# UFRJ - PPGI
# MAB719
# Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 2.7
"""

import Pmf
from first import weeks_first_preg
from first import weeks_non_first_preg
import matplotlib.pyplot as pyplot

def ConditionalAfter(pmf , w = 39):
    """
    Tests if the baby will born in w, given the baby wasn't born prior to w

    Args:
        pmf : the probability mass function
        w : the week

    Returns:
        float
    """
    
    filtered = {value : prob for value, prob in pmf.Items() if value >= w}

    prob = 0.0
    if (len(filtered) > 0):
        filtered_pmf = Pmf.MakePmfFromDict(filtered)
        filtered_pmf.Normalize()
        prob = filtered_pmf.Prob(w)
        
    return prob

def main():

    pmf_1st = Pmf.MakePmfFromList(weeks_first_preg)
    pmf_non = Pmf.MakePmfFromList(weeks_non_first_preg)

    weeks = range(20, 50)
    conditionals_1st = [ConditionalAfter(pmf_1st, i) for i in weeks ]
    conditionals_non = [ConditionalAfter(pmf_non, i) for i in weeks ]

    print conditionals_1st
    print conditionals_non

    
    #pyplot.hist([conditionals_1st , conditionals_non], normed = 1)
    pyplot.plot(weeks, conditionals_1st, 'b*-' , label="first")
    pyplot.plot(weeks, conditionals_non, 'ro-' , label="others")
    pyplot.legend()
    pyplot.show()

if __name__ == '__main__':
    main()
