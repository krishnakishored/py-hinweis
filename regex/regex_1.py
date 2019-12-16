#!/usr/bin/python
import re


def regex_fn_1():
    '''
    Let’s find the words before and after the word 'to'
    The first group (.*) identified the string: Learn and the next group (*.?) identified the string: Analyze.
    '''
    line = "Learn to Analyze Data with Scientific Python";
    # re.match(pattern, string, flags=0)
    m = re.match( r'(.*) to (.*?) .*', line, re.M|re.I)

    if m:
        print("m.group() : ", m.group())
        print( "m.group(1) : ", m.group(1))
        print("m.group(2) : ", m.group(2)) 
    else:
        print("No match!!") 


if __name__=="__main__":
    regex_fn_1()   