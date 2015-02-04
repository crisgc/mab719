#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
UFRJ - PPGI
MAB719
Cristiano Gurgel de Castro

ThinkStats: Exe 3.1
"""

import myheader
import Pmf

def unbias_pmf(pmf):
    """
    Remove the bias from a Probability Mass Function which was produced from a
    survey

    @type pmf: Pmf.Pmf

    Args:
        pmf: The PMF

    Side effect:
        Unbias the pmf
    """
    for (x,prob) in pmf.Items():
        pmf.Mult(x , 1.0 / x)

    pmf.Normalize()

def make_dist():
    """
    Returns:
        The class size distribution
    """
    class_size_dist = { 7: 8, 12: 8, 17: 14, 22: 4, 27: 6, 32:12, 37: 8, 42: 3,
            47: 2 }
    return class_size_dist

def main():
    # Classes by mid-size
    class_size_dist = make_dist()
    pmf = Pmf.MakePmfFromDict(class_size_dist, "Classes dist")
   
    mean = pmf.Mean()

    unbiased_pmf = pmf.Copy()
    unbias_pmf(unbiased_pmf)

    print "Mean Class size: %.3f" % mean
    print "Suposing the data comes from interview (Mean): %.3f" % \
        unbiased_pmf.Mean()


if __name__ == "__main__":
    main()
