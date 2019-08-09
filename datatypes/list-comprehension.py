# https://www.python-course.eu/python3_list_comprehension.php



def comprehension_list_2():
    shark_letters = [letter for letter in 'shark']
    print(shark_letters) # ['s', 'h', 'a', 'r', 'k']
    odd_num_list = [num for num in range(1,10,2)]
    print(odd_num_list) # [1, 3, 5, 7, 9]
    fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
    fish_list = [fish for fish in fish_tuple if fish != 'octopus']
    print(fish_list)

    nested_if_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
    print(nested_if_list)
        
    even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
    print(even_squares)

    my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
    print(my_list) # [40, 80, 120, 80, 160, 240, 120, 240, 360]

def comprehension_list_1():
    Celsius = [39.2, 36.5, 37.3, 37.8]
    Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
    
    print(Fahrenheit)    

    # A Pythagorean triple consists of three positive integers a, b, and c, such that  a2 + b2 = c2. 
    triplet = [(x,y,z)  for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
    # the following generates duplicates too
    # triplet = [(x,y,z)  for x in range(1,30) for y in range(1,30) for z in range(1,30) if x**2 + y**2 == z**2]
    print(triplet) # [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]



    #Cross Product - A×B = {(a, b) : a belongs to A, b belongs to B}. 
    colours = [ "red", "green", "yellow", "blue" ]
    things = [ "house", "car", "tree" ]
    coloured_things = [ (x,y) for x in colours for y in things ]
    # coloured_things = [ x+' '+y for x in colours for y in things ]
    print(coloured_things)
    
    '''
    Generator Comprehension
    They are simply like a list comprehension but with parentheses - instead of (square) brackets around it. 
    but a generator comprehension returns a generator instead of a list.  
    '''
    Fahrenheit_gen = (((float(9)/5)*x + 32) for x in Celsius )
    print(Fahrenheit_gen) # <generator object comprehension_list_1.<locals>.<genexpr> at 0x10c3e26d8>
    print(type(Fahrenheit)) # <class 'list'>
    print(type(Fahrenheit_gen)) # <class 'generator'>
    print(list(Fahrenheit_gen)) # [102.56, 97.7, 99.14, 100.03999999999999]
    # gernerator - only once it's valid
    # print(list(Fahrenheit_gen))# []
    # print(tuple(Fahrenheit_gen)) # ()

    x = (x**3 for x in range(10))
    print(x) #<generator object <genexpr> at 0x10c4a3840>
    for i in x:
        print(i, end=" ")
    
def primes_using_sieve_of_eratosthenes(n):
    from math import sqrt
    # n = 100
    sqrt_n = int(sqrt(n))    

    #the sieve of Eratosthenes
    no_primes = [j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)]
    # print(no_primes)# lots of double entries - use set comprehension to resolve
    '''
    A set comprehension is similar to a list comprehension, but returns a set and not a list. 
    Using Set comprehension, we are able to create the set of non primes without doublets:
    '''
    no_primes_set = {j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)}
    # print(no_primes_set)
    
    # primes = [x for x in range(2,n) if x not in no_primes]
    primes = [x for x in range(2,n) if x not in no_primes_set]
    print(primes)

# Recursive Function to Calculate the Primes
def primes(n):
    from math import sqrt
    if n==0:
        return []
    elif n==1:
        return []
    else:
        # it is enough to examine the multiples of the prime numbers up to the square root of n
        p = primes(int(sqrt(n))) 
        no_p = {j for i in p for j in range(i*2, n+1, i) }
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p

    
###############################################################################
# https://www.hackerrank.com/challenges/list-comprehensions/problem
def hr_listcomprehension(x,y,z,n):
    return [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]


# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem 
def hr_second_max(mylist):
    temp = mylist.copy()
    first_max = max(temp)
    while max(temp) == first_max:
        temp.remove(first_max)
    return max(temp)


# https://www.hackerrank.com/challenges/nested-list/problem
def nested_lists_second_min(marksheet):
    # print([marks for name, marks in marksheet]) # [37.21, 37.21, 37.2, 41.0, 39.0]
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
    # print('\n'.join([a[0] for a in sorted(marksheet) if a[1] == second_highest]))
     

if __name__ == "__main__":
    # comprehension_list_1()
   
    # primes_using_sieve_of_eratosthenes(100)
    
    # print(primes(100))    

    # for i in range(1,20):
    #     print(i, primes(i))

    # comprehension_list_2()
    # print(hr_listcomprehension(1,1,1,2))
    # print(hr_listcomprehension(2,2,2,2))

    # mylist = [2,3,6,6,5]
    # print(hr_second_max(mylist))

    # nested_lists_second_min
    # marksheet=[]
    # for _ in range(int(input())):
        # name = input()
        # score = float(input())
        # marksheet.append([name,score]) # build a nested list
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]

    print(marksheet)
    nested_lists_second_min(marksheet)   
    