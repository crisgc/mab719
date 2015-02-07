#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
# UFRJ - PPGI
# MAB719
# Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 1.3
"""

def RemainingLifetime(age , pmf):
    freq_map = pmf.GetDict()
    freq_filter = { key : value for key, value in iteritems(freq_map) if key >=
            age  }
    new_pmf = MakePmfFromDict (freq_filter)
    new_pmf.Normalize()
    return new_pmf

