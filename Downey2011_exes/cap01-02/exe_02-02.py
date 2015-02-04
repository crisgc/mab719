#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
# UFRJ - PPGI
# MAB719
# Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 2.2
"""

import thinkstats
import first
import math

if __name__ == '__main__':
    mean_1st, var_1st = thinkstats.MeanVar(first.weeks_first_preg)
    sd_1st = math.sqrt(var_1st)
    mean_non1st, var_non1st = thinkstats.MeanVar(first.weeks_non_first_preg)
    sd_non1st = math.sqrt(var_non1st)

    tuple_1st = (mean_1st, var_1st, sd_1st)
    tuple_non = (mean_non1st, var_non1st, sd_non1st)

    print '(Mean, var, sd)'
    print '1st: (%.3f, %.3f, %.3f)' % tuple_1st
    print 'non1st: (%.3f, %.3f, %.3f)' % tuple_non
    print 'diffs: (%.3f h, %.3f h^2, %.3f h)' % tuple([24 * 7 * (first - non) for first, non in
        zip(tuple_1st, tuple_non)]) 
    print 'diffs norms (%%): (%.3f, %.3f, %.3f)' % tuple([100.0 * (first - non)/first for first, non in
        zip(tuple_1st, tuple_non)]) 
    
