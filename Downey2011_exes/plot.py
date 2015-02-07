"""
Cristiano G Castro

Functions for plotting a pmf
"""

import numpy
from Pmf import Hist
import matplotlib.pyplot as plt

def plot_histogram(hist, xlabel=None, ylabel=None):
    """
    Plots a histogram

    @type hist: Hist

    Args:
        hist: the histogram

    """
    (x,w) = hist.Render();

    plt.hist(x, bins = max(x), weights=w)

    if not xlabel is None: plt.xlabel(xlabel)
    if not ylabel is None: plt.ylabel(ylabel)
    plt.show()

