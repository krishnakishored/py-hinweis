import pandas as pd
import numpy as np


def basic_series():
    S = pd.Series(
        [11, 28, 72, 3, 5, 8]
    )  # created a default index starting with 0 going to 5
    # print(S)
    print(S.index)  # RangeIndex(start=0, stop=6, step=1)
    print(S.values)  #  same as ndarrays of Numpy
    X = np.array([11, 28, 72, 3, 5, 8])
    print(
        type(S.values), type(X)
    )  # <class 'numpy.ndarray'> <class 'numpy.ndarray'>

    fruits = ["apples", "oranges", "cherries", "pears"]
    quantities = [20, 33, 52, 10]
    S = pd.Series(quantities, index=fruits)
    print(
        S.index
    )  # Index(['apples', 'oranges', 'cherries', 'pears'], dtype='object')
    print(S.values)


def add_two_series():
    """
    The indices do not have to be the same for the Series addition.
    The index will be the "union" of both indices.
    If an index doesn't occur in both Series, the value for this Series will be NaN:

    o/p:
    cherries       83.0
    oranges        46.0
    peaches         NaN
    pears          42.0
    raspberries     NaN
    dtype: float64

    # >>> np.sin(S)
    apples      0.912945
    oranges     0.999912
    cherries    0.986628
    """
    fruits = ["peaches", "oranges", "cherries", "pears"]
    fruits2 = ["raspberries", "oranges", "cherries", "pears"]
    S = pd.Series([20, 33, 52, 10], index=fruits)
    S2 = pd.Series([17, 13, 31, 32], index=fruits2)
    print(S + S2)
    print("sum of S: ", sum(S))  # sum of S:  115

    # Indexing
    # print(S[['apples', 'oranges', 'cherries']]) # Error in future
    """Series objects can also be accessed by multiple indexes at the same time.
    This can be done by packing the indexes into a list."""
    S = pd.Series([20, 33, 52], index=["apples", "oranges", "cherries"])
    print(S.reindex(["apples", "oranges", "cherries"]))

    """Similar to Numpy we can use scalar operations or mathematical functions on a series:"""
    print((S + 3) * 4)
    print(np.sin(S))

    """pandas.Series.apply"""
    print(S.apply(np.log))
    print(S.apply(lambda x: x if x > 50 else x + 10))

    """Filtering with a Boolean array"""
    print(S[S < 50])
    print("apples" in S)  # True


def series_from_dict():
    cities = {
        "London": 8615246,
        "Berlin": 3562166,
        "Madrid": 3165235,
        "Rome": 2874038,
        "Paris": 2273305,
        "Vienna": 1805681,
        "Bucharest": 1803425,
        "Hamburg": 1760433,
        "Budapest": 1754000,
        "Warsaw": 1740119,
        "Barcelona": 1602386,
        "Munich": 1493900,
        "Milan": 1350680,
    }

    city_series = pd.Series(cities)
    print(city_series)
    # Missing data  - NaN
    my_cities = ["London", "Paris", "Zurich", "Berlin", "Stuttgart", "Hamburg"]
    my_city_series = pd.Series(cities, index=my_cities)
    """Due to the Nan values the population values for the other cities are turned into floats."""
    print(my_city_series)  # dtype: float64

    """We can check for missing values with the methods isnull and notnull:"""
    print(my_city_series.isnull())
    print(my_city_series.notnull())
    """We get also a NaN, if a value in the dictionary has a None:"""
    d = {"a": 23, "b": 45, "c": None, "d": 0}
    print(pd.Series(d))
    """The Series method dropna returns a Series which consists only of non-null data:"""
    print(my_city_series.dropna())
    """Filling in Missing Data"""
    # print(my_city_series.fillna(100))

    d = {"a": 23, "b": 45, "c": None, "d": 0}
    missing = {"c": 597939}
    print(
        pd.Series(d).fillna(missing).astype(int)
    )  # appropriate filling using dictionaries
    """using fillna().astype(int) solves the problem of NaN getting filled with floats"""


if __name__ == "__main__":
    # basic_series()
    # add_two_series()
    series_from_dict()
