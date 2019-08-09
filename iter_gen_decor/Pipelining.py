from __future__ import print_function

import random
import time


'''
Generators can be used to pipeline commands similar to UNIX shell commands.
'''

#Creating a log files that is continuously updated.
def log(file_name):
    """Write some random log data"""
    fobj = open(file_name,'w')
    while True:
        value = random.randrange(0,50)
        if value < 10:
            fobj.write('# comment\n')
        else:
            fobj.write("%d\n" % value)
        fobj.flush()
        time.sleep(2)



#-------------------------------------------------------------------------------
#Now we can write a program with generators.
#We read the file and wait if there are currently no more new lines until new ones are written:
LIMIT = 1000
def read_forever(fobj):
    """Read from a file as long as there are lines. Wait for the other process to write more lines."""
    counter = 0
    while True:
        if counter > LIMIT:
            break
        line = fobj.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

#Then we filter out all the comment lines:
def filter_comments(lines):
    '''Filter out lines Starting with #'''
    for line in lines:
        if not line.strip().startswith('#'):
            yield line

#we convert the entry in the line into an integer
def get_number(lines):
    "Read the number in the line & convert it to an integer"
    for line in lines:
        yield int(line.split()[-1])


# Finally, we pipe all these together and calculate the sum of all numbers and print it on the screen:
def show_sum(file_name='out.txt'):
    "Start all the generators and calculate the sum continuously"
    lines = read_forever(open(file_name))
    filtered_lines = filter_comments(lines)
    numbers = get_number(filtered_lines)
    sum_ = 0
    try:
        for number in numbers:
            sum_ += number
            sys.stdout.write('sum:%d\r' % sum_)
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("sum:",sum_)


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
