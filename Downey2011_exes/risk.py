#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
# UFRJ - PPGI
# MAB719
# Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 2.6
"""

import Pmf
import math
import sys
import first

def calculateFreq( pmf , begin, end ):
    """
    Calculates the frequencies of the pmf betweer [begin, end)

    Args:
        pmf: the probability mass function
        begin: the first (inclusive) element of the interval
        end: the last (exclusive) element of the interval

    Return:
        the probability, to fall between [begin, end)

    Side effect
        Normalize the pmf

    """

    pmf.Normalize()
    items = pmf.GetDict() ;
    filtered = [ prob for value, prob in items.iteritems() 
            if value >= begin and value < end ] 
    prob_sum = math.fsum(filtered)
    return prob_sum

def ProbEarly(pmf):
    """
    Calculate the probability for a baby to arrive early, say with 37 or less
    weeks
    """
    prob = calculateFreq(pmf, 0 , 38)
    return prob

def ProbOnTime(pmf):
    """
    Calculates the probability for a baby to arrive on time, i.e between 38 and
    40 weeks
    """
    prob = calculateFreq(pmf, 38, 41)
    return prob

def ProbLate(pmf):
    """
    Calculate the probability for a baby to arrive late, i.e. 41 or more weeks
    """
    prob = calculateFreq(pmf, 41, sys.maxint)
    return prob

def AllProbs(pmf):
    result = (ProbEarly(pmf) , ProbOnTime(pmf) , ProbLate(pmf) )
    return result

def multByScalar(t , n = 100.0):
    """
    Multiply a tuple by a scalar
    """
    new = tuple([x * n for x in t])
    return new

def main():
    """
    Testing ... 
    """
    pmf_1st = Pmf.MakePmfFromList(first.weeks_first_preg)
    pmf_non = Pmf.MakePmfFromList(first.weeks_non_first_preg)
    pmf_all = Pmf.MakePmfFromList(first.weeks_all)

    all_probs_1st = AllProbs(pmf_1st)
    all_probs_non = AllProbs(pmf_non)
    all_probs_all = AllProbs(pmf_all)

    # TODO utilizar tabulate para imprimir melhor (http://goo.gl/OkEF5E)
    print "     (early , on time, late)"
    print "1st  (%.2f , %.2f , %.2f)" % multByScalar(all_probs_1st)
    print "non  (%.2f , %.2f , %.2f)" % multByScalar(all_probs_non)
    print "all  (%.2f , %.2f , %.2f)" % multByScalar(all_probs_all)

    risks = tuple([ f / non for f , non in zip(all_probs_1st,
        all_probs_non)])

    print 'Relative Risks (%2.3f , %2.3f , %2.3f)' % risks

if __name__ == '__main__':
    main()

