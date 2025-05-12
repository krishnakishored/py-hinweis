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
