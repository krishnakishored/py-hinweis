from collections import Counter


class Demo:
    def __init__(self):
        pass
        self.name = "Demo"

    def demonstrate_enumerate(self):
        """
        Demonstrates different ways to use enumerate() in Python

        enumerate() returns a tuple containing count (from start) and the value obtained from iterating over sequence
        """
        # Basic enumeration starting from 0
        fruits = ["apple", "banana", "cherry"]
        for i, fruit in enumerate(fruits):
            print(f"Index {i}: {fruit}")

        # Enumeration with custom start index
        for i, fruit in enumerate(fruits, start=1):
            print(f"Fruit #{i}: {fruit}")

        # Using enumerate with strings
        word = "Python"
        for i, char in enumerate(word):
            print(f"Position {i}: {char}")

        # Converting enumerate object to list of tuples
        seasons = ["Spring", "Summer", "Fall", "Winter"]
        enum_seasons = list(enumerate(seasons))
        print(f"List of enumerated tuples: {enum_seasons}")

        # Using enumerate in list comprehension
        indexed_seasons = [
            f"{i}: {season}" for i, season in enumerate(seasons)
        ]
        print(f"Indexed list: {indexed_seasons}")

    def demonstrate_counter(self):
        """
        Demonstrates various uses of collections.Counter in Python

        Counter is a dict subclass for counting hashable objects.
        It provides a dictionary where elements are stored as dictionary keys
        and their counts are stored as dictionary values.
        """
        # Basic Counter usage with a list
        colors = ["red", "blue", "red", "green", "blue", "blue"]
        color_counts = Counter(colors)
        print(
            f"Color counts: {color_counts}"
        )  # Counter({'blue': 3, 'red': 2, 'green': 1})

        # Counter with strings
        text = "mississippi"
        char_counts = Counter(text)
        print(
            f"Character counts: {char_counts}"
        )  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

        # Updating Counter
        more_colors = ["blue", "green", "yellow"]
        color_counts.update(more_colors)
        print(f"Updated counts: {color_counts}")

        # Most common elements
        print(f"Most common colors: {color_counts.most_common(2)}")

        # Operations with Counters
        counter1 = Counter(["a", "b", "c", "a"])
        counter2 = Counter(["a", "d", "e", "a"])

        # Addition of counters
        print(f"Counter1 + Counter2: {counter1 + counter2}")

        # Subtraction of counters
        print(f"Counter1 - Counter2: {counter1 - counter2}")

        # Intersection (taking minimum of each count)
        print(f"Counter1 & Counter2: {counter1 & counter2}")

        # Union (taking maximum of each count)
        print(f"Counter1 | Counter2: {counter1 | counter2}")

        # Converting to list of elements
        print(f"List of all elements: {list(color_counts.elements())}")

        # Getting count of a specific element
        print(f"Count of 'blue': {color_counts['blue']}")

        # Getting count of non-existent element (returns 0 instead of KeyError)
        print(f"Count of 'purple': {color_counts['purple']}")  # returns 0
