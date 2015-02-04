"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf
from bowl import Bowl

class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    bowls = {
            'Bowl 1': Bowl({ 'vanilla' : 30 , 'chocolate' : 10 }) ,
            'Bowl 2': Bowl({ 'vanilla' : 20 , 'chocolate' : 20 })
            }

    def __init__(self, hypos):
        """Initialize self.

        hypos: sequence of string bowl IDs
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        bowl = self.bowls[hypo]
        like = bowl.probability_of_flavors()[data]
        bowl.pick_a_cookie(data, like)
        bowl.print_state()
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)

    pmf.Update('vanilla')
    pmf.Update('chocolate')
    pmf.Update('vanilla')
    pmf.Update('vanilla')
    pmf.Update('vanilla')
    pmf.Update('vanilla')

    for hypo, prob in pmf.Items():
        print hypo, prob


if __name__ == '__main__':
    main()
