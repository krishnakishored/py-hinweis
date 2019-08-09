res_zip = list(zip([1,2,3],['a','b','c'])) #which takes any number of iterables as arguments and returns an iterator over tuples of their corresponding elements



if __name__=="__main__":
    # print(res_zip)
    # print(iter([1,2,3])) #<list_iterator object at 0x108d73f28>
    # print(iter(res_zip))
    # print(list(map(len,['abc','de','ghij']))) # [3,2,4]
    # print(list(map(sum,zip([1,2,3],[9,8,7]))))
    # print(list(map(len,zip(['abc','de','ghij'],['abc','de','ghij'])))) # [2,2,2]

    n = int(input())
    countries = []
    for country in range(n):
        countries.append(str(input("")))
    print(countries)



# Since iterators are iterable, you can compose zip() and map() to produce an iterator over combinations of elements in more than one iterable.     




# There are two main reasons why such an “iterator algebra” is useful: improved memory efficiency (via lazy evaluation) and faster execuction time. 

#https://realpython.com/python-itertools/


