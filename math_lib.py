from scipy.stats import itemfreq
import numpy as np


def frequency_distribution(items):
    return itemfreq(items)


def standard_deviation(items):
    return np.std(items)