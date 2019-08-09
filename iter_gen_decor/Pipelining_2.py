#While  generators  establish  a  pull  pipeline,  coroutines  can  create  a  push  pipeline
from __future__ import print_function
import random
import time

import functools
import sys

"""Creating a log files that is continuously updated.Modified version with log levels."""
LEVELS = ['CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'WARN']

def log(file_name):
    """Write some random log data"""
    fobj = open(file_name,'w')
    while True:
        value = random.randrange(0,50)
        if value < 10:
            fobj.write('# comment\n')
        else:
            fobj.write("%s: %d\n" % (random.choice(LEVELS),value))
        fobj.flush()
        time.sleep(2)

#--------------------------------------------------------------------------------

#We use our decorator to advance a coroutine to the first yield:
"""Use coroutines to sum log file data with different log levels."""

LIMIT = 1000

def init_coroutine(func):
    @functools.wraps(func)
    def init(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return init

#The function for reading the file line-by-line takes the argument target. This is a coroutine that will consume the line:
def read_forever(fobj, target):
    """Read from a file as long as there are lines.
    Wait for the other process to write more lines. Send the lines to `target`. """
    counter = 0
    while True:
        if counter > LIMIT:
            break
        line = fobj.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

#We have two coroutines that receive values with line = yield and send their their computed results to target:

@init_coroutine
def filter_comments(target):
    """Filter out all lines starting with #.
    """
    while True:
        line = yield
        if not line.strip().startswith('#'):
            target.send(line)

@init_coroutine
def get_number(targets):
    """Read the number in the line and convert it to an integer.
    Use the level read from the line to choose the to target.
    """
    while True:
        line = yield
        level, number = line.split(':')
        number = int(number)
        targets[level].send(number)

## Consumers for different cases.

@init_coroutine
def fatal():
    """Handle fatal errors """
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('FATAL sum: %7d\n' % sum_)

@init_coroutine
def critical():
    """Handle critical errors."""
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('CRITICAL sum: %7d\n' % sum_)

@init_coroutine
def error():
    """Handle normal errors."""
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('ERROR    sum: %7d\n' % sum_)

@init_coroutine
def warn():
    """Handle warnings."""
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('WARN     sum: %7d\n' % sum_)

@init_coroutine
def debug():
    """Handle debug messages."""
    sum_ = 0
    while True:
        value = (yield)
        sum_ += value
        sys.stdout.write('DEBUG    sum: %7d\n' % sum_)

#collect the coroutines in a dictionary
TARGETS = {'CRITICAL': critical(),
           'DEBUG': debug(),
           'ERROR': error(),
           'FATAL': fatal(),
           'WARN': warn()
           }

#Now we can start pushing the data through our coroutine pipeline:
def show_sum(file_name='out.txt'):
    """Start the pipline."""
    # read_forever > filter_comments > get_number > TARGETS
    read_forever(open(file_name), filter_comments(get_number(TARGETS)))

if __name__ == '__main__':
    import sys
    def test():
        """Start logging"""
        #import sys
        file_name = sys.argv[1]
        print("logging to ",file_name)
        log(file_name)

#    test() # to write random numbers
    show_sum(sys.argv[1])
