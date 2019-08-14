# https://python-course.eu/python3_sets_frozensets.php
# https://python-course.eu/python_sets_example.php

'''
A set contains an unordered collection of unique and immutable objects.
Though sets can't contain mutable objects, sets are mutable: 
'''

def set_basics_1():
    x = set("A Python Tutorial")
    print(x) # {'A', 'r', 'n', 'i', ' ', 't', 'T', 'o', 'P', 'l', 'h', 'a', 'y', 'u'}
    x = set(["Perl", "Python", "Java"])
    print(x) # {'Java', 'Perl', 'Python'}
    # pass a tuple with reappearing elements to the set function
    cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
    print(cities) # {'Lyon', 'Birmingham', 'London', 'Berlin', 'Paris'} # removes doublets
    print(set((("Python","Perl"), ("Paris", "Berlin", "London")))) # {('Python', 'Perl'), ('Paris', 'Berlin', 'London')}
    # cities = set((["Python","Perl"], ["Paris", "Berlin", "London"])) # TypeError: unhashable type: 'list'
    cities.add("Strasbourg")
    # sets are mutable but can't contain mutable objects
    print(cities) # {'London', 'Birmingham', 'Berlin', 'Lyon', 'Strasbourg', 'Paris'}
    '''
    Frozensets are like sets except that they cannot be changed, i.e. they are immutable
    '''
    f_cities = frozenset(["Frankfurt", "Basel","Freiburg"])
    # f_cities.add("Strasbourg") # AttributeError: 'frozenset' object has no attribute 'add'
    '''new notation - { }'''
    adjectives = {"cheap","expensive","inexpensive","economical"} 
    
    '''
    set operations - add, clear, 
    '''
    cities.clear()
    print(cities) # set()

    '''Creates a shallow copy, which is returned.'''
    more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
    cities_backup = more_cities.copy()
    # more_cities.clear()
    # print(more_cities) # set()
    print(cities_backup) # {'Schaffhausen', 'St. Gallen', 'Winterthur'}
    cities_backup_assignment = more_cities
    more_cities.clear()
    print(cities_backup_assignment) # set()   

    '''
    difference()
    Instead of using the method difference, we can use the operator "-"
    difference_update() removes all elements of another set from this set. 
    x.difference_update(y) is the same as "x = x - y"

    '''
    x = {"a","b","c","d","e"}
    y = {"b","c"}
    z = {"c","d"}
    print(x.difference(y)) # {'e', 'd', 'a'}
    print(x.difference(y).difference(z)) # {'a', 'e'}
    print(z-y) # {'d'}

    x = {"a","b","c","d","e"}
    y = {"b","c"}
    print(x.difference_update(y)) # None
    print(x) # {'e', 'a', 'd'}

def set_basics_2():
    '''
    discard(el): An element el will be removed from the set, if it is contained in the set. 
    If el is not a member of the set, nothing will be done.

    remove(el): works like discard(), but if el is not a member of the set, a KeyError will be raised.

    pop() removes and returns an arbitrary set element. The method raises a KeyError if the set is empty
    '''

    x = {"a","b","c","d","e"}
    y = {"c","d","e","f","g"}
    print(x.union(y)) # {'b', 'f', 'a', 'c', 'e', 'd', 'g'}
    print(x.intersection(y)) # {'e', 'c', 'd'}
    print(x.isdisjoint(y)) # This method returns True if two sets have a null intersection.
    z = {"c","d"}
    print(x.issubset(z)) # False
    print(x.issuperset(z)) # True




if __name__ == "__main__":
    # set_basics_1()
    set_basics_2()