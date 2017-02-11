from scipy.stats import itemfreq
from scipy import mean
import numpy as np


def frequency_distribution(items):
    return itemfreq(items)


def standard_deviation(items):
    return np.std(items)


def transpose(matrix):
    return np.array(matrix).transpose()


def ljust(self, n, fillvalue=''):
    return self + [fillvalue] * (n - len(self))
