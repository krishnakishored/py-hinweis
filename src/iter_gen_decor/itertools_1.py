# https://realpython.com/python-itertools/
"""
the functions in itertools “operate” on iterators to produce more complex iterators
    - zip_longest()
    - combinations()
    - permutations()
    - count()

    - combinations_with_replacement()
"""


def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i * n : (i + 1) * n]) for i in range(num_groups)]


def better_grouper(inputs, n):
    """
    The expression [iters(inputs)] * n creates a list of n references to the same iterator
    """
    iters = [iter(inputs)] * n
    """
    Next, zip(*iters) returns an iterator over pairs of corresponding elements of each iterator in iters.
    When the first element, 1, is taken from the “first” iterator, the “second” iterator now starts at 2 since it is just a reference to the “first” iterator and has therefore been advanced one step.
    So, the first tuple produced by zip() is (1, 2).
    At this point, “both” iterators in iters start at 3, so when zip() pulls 3 from the “first” iterator, 
    it gets 4 from the “second” to produce the tuple (3, 4). 
    This process continues until zip() finally produces (9, 10) and “both” iterators in iters are exhausted:
    """
    return zip(*iters)


def better_grouper_2(inputs, n, fillvalue=None):
    import itertools as it

    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)


def itertools_1():
    import itertools as it

    res_zip = list(zip([1, 2, 3], ["a", "b", "c"]))
    print(res_zip)  # [(1, 'a'), (2, 'b'), (3, 'c')]
    print(iter([1, 2, 3, 4]))  # <list_iterator object at 0x1085d90b8>
    # print(iter(res_zip))
    print(list(map(len, ["abc", "de", "fghi"])))  # [3,2,4]
    """
    Since iterators are iterable, you can compose zip() and map() to produce an iterator over combinations of elements in more than one iterable. 
    """
    print(list(map(sum, zip([1, 2, 3], [9, 8, 7]))))  # [10, 10, 10]
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(naive_grouper(nums, 2))  # [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    print(better_grouper(nums, 2))  # <zip object at 0x10a0fafc8>
    print(
        list(better_grouper(nums, 2))
    )  # [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    print(
        list(better_grouper(nums, 4))
    )  # [(1, 2, 3, 4), (5, 6, 7, 8)] # doesn't handle if n is not a factor of length

    x = [1, 2, 3, 4, 5]
    y = ["a", "b", "c"]
    print(list(zip(x, y)))
    print(
        list(it.zip_longest(x, y))
    )  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]
    print(
        list(better_grouper_2(nums, 4))
    )  # [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, None, None)]


def itertools_2():
    """
    You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
    How many ways can you make change for a $100 dollar bill?
    """
    import itertools as it

    bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    makes_100 = []
    for n in range(1, len(bills) + 1):
        for combination in it.combinations(bills, n):
            if sum(combination) == 100:
                makes_100.append(combination)

    # print(makes_100)
    print(set(makes_100))
    """
    {(20, 20, 10, 10, 10, 10, 10, 5, 1, 1, 1, 1, 1),
        (20, 20, 10, 10, 10, 10, 10, 5, 5),
        (20, 20, 20, 10, 10, 10, 5, 1, 1, 1, 1, 1),
        (20, 20, 20, 10, 10, 10, 5, 5),
        (20, 20, 20, 10, 10, 10, 10)}
    """

    # combinations_with_replacement() works just like combinations(), accepting an iterable inputs and a positive integer n,
    # and returns an iterator over n-tuples of elements from inputs.
    # The difference is that combinations_with_replacement() allows elements to be repeated in the tuples it returns.
    print(
        list(it.combinations_with_replacement([1, 2], 2))
    )  # [(1, 1), (1, 2), (2, 2)]
    print(list(it.combinations([1, 2], 2)))  # [(1,2)]

    print("revised solution:")
    bills = [5, 2, 1]
    makes_100_B = []
    for n in range(1, 10):
        for combination in it.combinations_with_replacement(bills, n):
            if sum(combination) == 10:
                makes_100_B.append(combination)

    print(len(makes_100_B))  # 9
    print(list(it.permutations(["a", "b", "c"])))


def evens():
    """Generate even integers, starting with 0."""
    n = 0
    while True:
        yield n
        n += 2


def odds():
    """Generate even integers, starting with 0."""
    n = 1
    while True:
        yield n
        n += 2


def itertools_3():
    import itertools as it

    myevens = evens()
    myodds = odds()
    print(list(next(myevens) for _ in range(5)))  # [0, 2, 4, 6, 8]
    print(list(next(myodds) for _ in range(5)))  # [1, 3, 5, 7, 9]
    counter = it.count()
    print(list(next(counter) for _ in range(5)))  # [0, 1, 2, 3, 4]
    myevens_2 = it.count(step=2)
    myodds_2 = it.count(start=1, step=2)
    print(list(next(myevens_2) for _ in range(5)))  # [0, 2, 4, 6, 8]
    print(list(next(myodds_2) for _ in range(5)))  # [1, 3, 5, 7, 9]
    count_with_floats = it.count(start=0.5, step=0.75)  # count with floats
    print(
        list(next(count_with_floats) for _ in range(5))
    )  # [0.5, 1.25, 2.0, 2.75, 3.5]
    negative_count = it.count(start=-1, step=-0.5)
    print(
        list(next(negative_count) for _ in range(5))
    )  # [-1, -1.5, -2.0, -2.5, -3.0]
    """enumerated a list without a for loop without knowing the length of the list ahead of time."""
    print(
        list(zip(it.count(), [11, 22, 33, 44]))
    )  # [(0, 11), (1, 22), (2, 33), (3, 44)]


def fibs():
    """second order recurrence relation"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def itertools_4():
    fib = fibs()
    print(list(next(fib) for _ in range(6)))  # [0, 1, 1, 2, 3, 5]


if __name__ == "__main__":
    itertools_1()
    # itertools_2()
    # itertools_3()
    # itertools_4()
