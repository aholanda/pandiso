#!/usr/bin/env python3
"""TODO: doc"""

import os

from data import data
from plot import plot

# Research project information
__author__ = 'Adriano J. Holanda'
__copyright__ = 'Copyright 2021, University of São Paulo'
__credits__ = ['Adriano J. Holanda']
__license__ = "Unilicense"
__version__ = '0.1.0'
__maintainer__ = 'Adriano J. Holanda'
__email__ = 'aholanda@usp.br'
__status__ = 'dev'


DEFAULT_DATA_FN = os.path.join(data.dir(), 'covid19-sp-BR.csv')

if __name__ == '__main__':
    fn = DEFAULT_DATA_FN
    dt = 5

    # Data processing
    data = data()
    data.read(fn)
    data.group_by_time_interval(data, dt)

    # Plotting
    # Example of logistic function plot
    lplt = plot()
    lplt.logistic_example()
    # Applying the method to an empirical case
    parms = lplt.fit(data)
    lplt.estimate(data, parms)
