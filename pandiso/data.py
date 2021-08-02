"""TODO: doc"""
import sys
from typing import Dict

# Local module(s)
from helpers import  Error, fatal, info


class data(object):
    def __init__(self) -> None:
        super().__init__()
        self.data = None
        self.data_dt = None
        self.dt = 1
        # Last date of the first time step
        self.t_initial_date = '0000-00-00'
        # Last date of the last time step
        self.t_final_date = '0000-00-00'
        # Number of time steps
        self.t_steps = 0

    @staticmethod
    def dir():
        """Return the default local directory where data files 
        are located.
        """
        return 'data'

    def read(self, filename) -> None:
        """TODO: doc"""
        self.data = {}
        self.filename = filename
        with open(self.filename, 'r') as file:
            for ln, line in enumerate(file):
                if line.startswith('#'):
                    continue
                line = line.rstrip('\r\n')
                cols = line.split(";")
                self.data[cols[0]] = (int(cols[1]), float(cols[2]))
        info(f">>> data.read({self.filename})  # {ln} lines")

    def group_by_time_interval(self, data, dt: int, cumulative=True) -> Dict:
        """TODO: doc"""
        if self.data == None:
            fatal('run data.read(filename) first!', Error.DATA_NOT_READ)

        self.dt = dt
        self.data_dt = {}
        cases = 0
        isolevel = 0.0
        for t, (date, datum) in enumerate(self.data.items()):            
            cases += datum[0]
            isolevel += datum[1]
            if (t+1) % dt == 0:
                self.t_steps += 1
                if self.t_steps == 1:
                    self.t_initial_date = date
                # get the isolation level average
                isolevel /= dt
                self.data_dt[date] = (cases, isolevel)
                # reset
                isolevel = 0.0
                if not cumulative:
                    cases = 0
                # update final time step
                self.t_final_date = date

    def time_interval(self):
        return self.dt

    def per_time_interval(self):
        if self.data_dt == None:
            fatal('run data.group_per_time_interval() first!',
                    Error.DATA_NOT_PROCESSED)
        return self.data_dt

    def initial_date(self) -> str:
        return self.t_initial_date

    def final_date(self) -> str:
        return self.t_final_date

    def time_steps(self) -> int:
        return self.t_steps

    def print_date_bounds(self) -> None:
        info(f'* Initial date: {self.initial_date()}\n'
             f'* Final date: {self.final_date()}\n'
             f'* Number of time steps: {self.time_steps()}')