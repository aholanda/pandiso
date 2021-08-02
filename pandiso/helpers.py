"""TODO: doc"""

from enum import Enum
import sys

class Error(Enum):
    """Class to group error codes for the project, 
    each error code starts with module name in uppercase.
    """
    # data.py module
    DATA_NOT_READ = 1<<1
    DATA_NOT_PROCESSED = 1<<2

    # model.py module
    MODEL_VALUE_OUT_OF_BOUNDS = 1<<3

def fatal(msg: str, errno: int) -> None:
    """Print a message into standard error output and exit
    with the error code defined in the class Error.
    
    Parameters:
        msg   (str): error message to print
        errno (int): integer error code to pass to exit function
    """
    print(f'FATAL: {msg}', file=sys.stderr)
    sys.exit(errno)


def print_header(title: str) -> None:
    """An utility function to print a header to separate
    the sections.

    Parameter:
    ----------
    title (str): the title of the header
    """
    title = '\n' + '*'*32 + ' ' + title + ' ' + '*'*48
    print(title, file=sys.stderr)


def info(msg: str) -> None:
    """Print a message to the standard error.
    
    Parameter
    ---------
        msg (str): message to print
    """
    print(msg, file=sys.stderr)