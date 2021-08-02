"""TODO: doc"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import sys

# Local
from data import data
from helpers import print_header, info
from model import exp_logistic, differential_logistic

class plot(object):
    FIG_EXT = '.png'
    def __init__(self) -> None:
        super().__init__()

    def fit(self, data):
        """Plot the empirical data and its fitting using 
        logistic function.

        Parameters:
        ----------
        data_dt (List): a list of values sampled in a time interval.
        dt (int)      :  time interval used to sample the data.

        Return:
        ------
            A tuple with the fitting parameters

        """
        print_header('Fitting')
        fn = 'fig2' + plot.FIG_EXT
        dt = data.time_interval()
        data_dt = data.per_time_interval()

        # A sequence on integers to represent the time
        xs = np.arange(len(data_dt))

        # Empirical data: cumulative number of cases
        ys = [y for (y, _) in data_dt.values()]

        # Fitting
        popt, _ = curve_fit(exp_logistic, xs, ys, bounds=([0,0,0],np.inf), maxfev=1000)
        r, n_0, k = popt
        # Generate data using parameters from fitting
        ys_fitted = exp_logistic(xs, r, n_0, k)
        info('* Estimated parameters for exponential logistic function using empirical data:\n\t'
              r'[r_logistic=%1.3f, n_0=%d, k=%d]' % (r, n_0, k))

        plt.clf()
        plt.plot(xs, ys, '.')
        plt.plot(xs, ys_fitted, 'b-', lw=2)
        plt.legend(['empirical', 'fitted'], loc=2)
        plt.title(f'Cumulative number of cases using {dt} days as time step', fontsize='10')
        plt.grid()
        plt.xlabel('t')
        plt.ylabel('N')
        plt.savefig(fn)
        info(f'* Wrote {fn}')

        # Check correlation between empirical data and fitting
        # using logistic function
        r_pearson, p_value = stats.pearsonr(ys, ys_fitted)
        info('* Pearson correlation - empirical data x fitting model:\n\t'
                r'[r_pearson=%1.3f, p-value=%.2e]' % (r_pearson, p_value))
        data.print_date_bounds()

        return popt

    def estimate_cases(self, levels, fitted_parms):
        """TODO: doc"""
        cases_estimated = np.zeros(len(levels)) # TODO: test    
        avg_level = np.average(levels)
        std_level = np.std(levels)
        info(r'>>> average_isolation_level, standard_deviation=%1.4f, %1.4f'
                % (avg_level, std_level))
        # TODO: eliminate loop
        r, n_0, k = fitted_parms  # TODO: test
        beta = r*avg_level
        info(r'>>> beta=r_logistic*average_isolation_level # %1.4f*%1.4f=%1.4f' 
                % (r, avg_level, beta))
        for t in range(1, len(levels)):
            # Shift cases to view the effect of distancing
            r = beta / levels[t-1]
            cases_estimated[t] = exp_logistic(t, r, n_0, k)

        return cases_estimated


    def estimate(self, data, fit_parms):
        """TODO: doc"""
        print_header('Estimating')
        fn = 'fig3' + plot.FIG_EXT
        
        dt = data.time_interval()
        data_dt = data.per_time_interval()

        # A sequence on integers to represent the time
        xs = np.arange(len(data_dt))

        # Empirical data: cumulative number of cases
        ys_cases = [y for (y, _) in data_dt.values()]

        # Empirical data: isolation level
        ys_level = [y for (_, y) in data_dt.values()]

        # Estimate the number of cases at each time interval
        # using the fitting parameters.
        ys_cases_estimated = self.estimate_cases(ys_level, fit_parms)

        plt.clf()
        plt.subplot(2, 1, 1) 
        figlabel_locx = -19
        yfactor = 1.05
        plt.text(figlabel_locx, np.max(ys_cases)*yfactor, 'a)', style='normal', fontsize='12')  
        plt.plot(xs, ys_cases, '.')
        plt.plot(xs[:-1], ys_cases_estimated[:-1], 'b-', lw=2)
        plt.title(f'Cumulative number of cases using {dt} days as time step', fontsize='10')    
        plt.legend(['empirical', 'estimated'], loc=2)
        plt.grid()
        plt.ylabel('N')

        plt.subplot(2, 1, 2)
        plt.text(figlabel_locx, np.max(ys_level)*yfactor, 'b)', style='normal', fontsize='12')
        plt.title(f'Isolation levels using {dt} days as time step', fontsize='10')
        plt.plot(xs, ys_level, 'bx')
        plt.ylabel('average isolation level', fontsize='8')
        plt.subplots_adjust(left=0.125,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.2, 
                            hspace=0.35)
        plt.grid()
        plt.xlabel('t')
        plt.savefig(fn)
        info(f'* Wrote {fn}')
        r_pearson, p_value = stats.pearsonr(ys_cases[:-1], ys_cases_estimated[:-1])
        info('* Pearson correlation - empirical data x estimated cases:\n\t'
                r'[r_pearson=%1.3f, p_value=%.2e]' % (r_pearson, p_value))
        data.print_date_bounds()
                
    def logistic_example(self):
        fn = 'fig1' + plot.FIG_EXT
        # Time span
        t_final = 140  # final time
        ts = xs = np.arange(0, t_final)
        r = .1
        k = 1.0
        n_initial = 0.001  # Initial number of cases (normalized)
        ys = differential_logistic(n_initial, ts, r, k)
        plt.plot(xs, ys)
        plt.text(xs[2], k*.9, '$k={}$\n$r={}$'.format(k, r), 
                    fontsize=12)
        # Sigmoid midpoint
        mid = int(t_final/2) - 1
        plt.plot(mid, ys[mid], 'ro')
        plt.text(1.05*mid, ys[mid], 'midpoint', fontsize=10)
        plt.title('Logistic function')
        plt.grid()
        plt.xlabel('t')
        plt.ylabel('n(t)')
        plt.savefig(fn)
        info(f'* Wrote {fn}')
    