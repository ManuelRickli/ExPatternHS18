import numpy as np
from scipy.stats import multivariate_normal


class MVND:
    # TODO: EXERCISE 2 - Implement mean and covariance matrix of given data
    def __init__(self, data, p=1.0):
        self.p = p
        self.data = data
        self.mean = ???
        self.cov  = ???

    # TODO: EXERCISE 2 - Implement pdf and logpdf of a MVND
    def pdf(self, x):
        return ???
    
    def logpdf(self, x):
        return ???
