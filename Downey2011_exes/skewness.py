# coding=utf8

from Pmf import Hist
import survey
from plot import plot_histogram
import scipy.stats as sts
import numpy as np

def Skewness(values, mu=None):
    """
    Calculate the skewness of a number of values

    Args: 
        values: the data set
        mu: the optionally previous calculated mean

    Returns:
        the Skewness of the distribution
    """

    g1 = None
    
    if len(values):
        if mu is None:
            mu = np.mean(values)

        m2 = np.mean((values - mu) ** 2)
        m3 = np.mean((values - mu) ** 3)

        g1 = m3 / (m2 ** (3.0 / 2.0))
        
    return g1

def PearsonSkewness(values, mu=None, std=None, median=None):
    """
    Calculates the Pearson Skewness of some values

    Args:
        values: the data
        mu: the mean
        std: the standard deviation
        media: the median

    Returns:
        A float number tha representes de Pearson Skewness
    """
    if np.size(values):
        if mu is None:
            mu = np.mean(values)

        if std is None:
            std = np.std(values)

        if median is None:
            median = np.median(values)
        
        gp = 3.0 * float( mu - median ) / std
        return gp

def pregnancy_length_list(pregs):
    """
    Gets the pregnancy length list

    Args:
        pregs: the pregnancies from the DB

    Returns:
        the lengths of the pregnancies
    """
    lengths = [ record.prglength for record in pregs.records if record.outcome
            == 1 ]
    return lengths

def main():
    pregs = survey.Pregnancies()
    pregs.ReadRecords()
    lengths = pregnancy_length_list(pregs) ;
    hist = Hist();
    for l in lengths:
        hist.Incr(l)
        
    print 'The skewness of the pregnacy lengths is: ', Skewness(lengths)
    print 'The pearson skewness of the pregnacy lengths is: ', PearsonSkewness(lengths)
    plot_histogram(hist, xlabel='weeks', ylabel='number of births')
   
   
if __name__ == '__main__':
    main()
