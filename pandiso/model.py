"""TODO: doc"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys
from typing import List

# Local module(s)
from helpers import fatal, Error


def exp_logistic(t, r: float, n_0: float, k: float):
    """Logistic function in the exponential form:

    𝑓(t)= k / (1 + ((k-n_0)/n_0) * 𝑒^{−rt})

    Parameters
    ----------
    t   (List):  a list of values representing the time
    n_0 (float): sigmoid's midpoint
    k   (float): the maximum value for n;
    r   (float): the logistic growth rate.

    Return
    -------
    a list of values of f(t)

    """
    return k / (1 + ((k - n_0)/n_0)*np.exp(-r*t))


def __diff_logistic(n: int, ts: List[int], r: float, k: int):
    """Logistic function in the derivative form:

    dn/dt = r*n(t) * (1 - n(t)/k)

    Parameters
    ----------
    n (float)   : population (infected)
    t (int)     : time
    r (float)   : growth factor
    k (int)     : total population

    Returns:
        The dn/dt solution for each specified time interval in times ts.
    """
    if r < -1.0 or r > 1.0:
        fatal(f'r must be -1.0 < r <= 1.0, r={r}', 
                Error.MODEL_VALUE_OUT_OF_BOUNDS)

    dn_dt = r*n * (1 - n/k)
    return dn_dt


def differential_logistic(n_initial: int, ts: List[int], r: float, k: int):
    return odeint(__diff_logistic, n_initial, ts, args=(r, k))