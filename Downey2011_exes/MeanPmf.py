#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
# UFRJ - PPGI
# MAB719
# Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 2.5
"""

import Pmf

def PmfMean(pmf):
    """
    Calculates the mean of a probability mass function

    Side Effect:
        Normalize the pmf

    Args:
        pmf: the Probability Mass Function

    Returns:
        the mean of a non-empty pmf. None otherwise.
    """

    pmf.Normalize()
    mean = None
    items = pmf.Items()
    if (len(items) > 0):
        mean = 0.0
        for key,value in items:
            mean += key * value
    return mean

def PmfVar(pmf, mu = None):
    """
    Calculates the variance of a probability mass function

    Side Effect:
        Normalize the pmf

    Args:
        pmf: the probability mass function
        mu: The (previous calculated) mean

    Return:
        the variance of the distribution. Or None for a empty pmf.
    """
        
    # Tests if the mean was given
    if (mu is None):
        mu = PmfMean(pmf)

    items = pmf.Items()
    var = None
    if len(items) > 0 :
        var = 0.0
        for x, prob in items :
            var += prob * (x - mu)**2
    
    return var

if __name__ == '__main__':

    # Mean = 10.0 SD = 10.0
    dist = [ -8.6910e+0, 1.0860e+1, 2.0390e+1, 1.0270e+1, 6.3850e-1,
            1.1340e+1, 2.4110e+1, 8.4880e+0, 3.8790e+0, 6.0720e+0, 2.1070e+1,
            2.2150e+1, -8.5640e+0, 2.1340e+1, 2.1510e+1, 1.7740e+1, 1.6340e+1,
            3.7730e+0, -7.3710e+0, 1.3640e+1, 1.1170e+1, 8.4340e+0, 7.1910e+0,
            1.1760e+1, 1.6000e+1, 5.0780e+0, 1.1960e+1, 1.2150e+1, 1.5940e+1,
            -6.7600e+0, 2.0240e+1, 1.2820e+1, 3.9920e+0, 5.2610e+0, 6.2170e+0,
            1.8270e+0, 1.3820e+1, 1.1560e+1, 1.0320e+1, 2.2800e+1, 6.8070e+0,
            8.3660e+0, 9.1560e+0, 5.4340e+0, 2.0880e+1, 2.3800e+1, 1.0410e+1,
            1.2020e+0, 8.2040e+0, 1.0790e+1, 1.6770e+1, -2.1490e+0, -2.5960e+0,
            1.4220e+1, 4.6330e+0, 2.2910e+0, -1.2910e+1, 1.9790e+1, -1.1350e+1,
            -1.4030e+1, -8.8320e+0, -1.1910e+1, 2.7220e+1, 5.9580e+0, 3.0780e+0,
            1.8330e+0, 1.9760e+1, 1.8090e+1, 1.7970e+0, 1.2500e+1, 1.2710e+1,
            3.0650e+1, 1.4540e+1, 1.1790e+1, 1.0040e+1, -7.7290e+0, 1.8040e+1,
            5.7630e+0, 1.6420e+1, 2.6110e+1, 1.2150e+1, 1.7050e+1, 6.7680e+0,
            1.1070e+1, 1.2240e+1, 2.6530e+1, 1.5950e+1, -6.6580e+0, -9.6990e-1,
            2.6050e+1, 2.6700e+0, 8.9760e+0, 5.8690e+0, 2.6220e+1, 4.2780e+0,
            -1.5020e-1, -1.4240e-1, -6.1830e+0, 7.4210e+0, 1.4850e+1 ]

    pmf = Pmf.MakePmfFromList(dist)
    print 'Mean (my fun): %.3f' % PmfMean(pmf)
    print 'Mean (others): %.3f' % pmf.Mean()
    print 'Var (myfun)  : %.3f' % PmfVar(pmf)
    print 'Var (others) : %.3f' % pmf.Var()
    
