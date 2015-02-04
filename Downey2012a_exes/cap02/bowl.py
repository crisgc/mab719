"""
Cristiano Gurgel de Castro
ThinkBayes exe 2.1
"""

class Bowl(object):
    """
    A class that representes a bowl of cookues
    """

    def __init__(self, initial):
        """
        Args:
           initials: a dict that maps from a flavor to the number of cookies in
           the bowl
        """
        self.cookies = initial

    def pick_a_cookie(self, flavor, number):
        """
        Picks a cookie

        Args:
            flavor: the flavor of the cookie
            number: the number of cookies to pick. The tricky part to
            understand is that the number can be a real representing a
            probability.
        """
        self.cookies[flavor] -= number

    def probability_of_flavors(self):
        """
        Gets a dict witch maps from a flavor to the probability of one gets a
        cookie of that flavor from the bowl
        """
        n = self._total()
        probs = dict()
        for (flavor, number) in self.cookies.iteritems():
            probs[flavor] = float(number) / n

        return probs

    def _total(self):
        """
        Returns:
            the number of cookies in the bowl
        """
        return sum(self.cookies.itervalues())

    def print_state(self):
        print self.cookies 


