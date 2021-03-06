import numpy as np
from scipy.stats import multivariate_normal


class MVND:
    def __init__(self, data, p=1.0):
        self.p = p
        self.data = data
        self.mean = data.mean(1)
        self.cov  = np.cov(data)

    def pdf(self, x):
        return self.p * multivariate_normal.pdf(x, self.mean, self.cov)
    
    def logpdf(self, x):
        return np.log(self.p) + multivariate_normal.logpdf(x, self.mean, self.cov)
