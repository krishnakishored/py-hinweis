"""Helper to switch on and off logging of decorated functions."""
from __future__ import print_function
import functools

LOGGING = False

def logged(func):
    """Decorator for logging."""
    @functools.wraps(func)
    def _logged(*args, **kwargs):
        """Takes the arguments"""
        if LOGGING:
            print('logged') # do proper logging here
        return func(*args, **kwargs)
    return _logged
