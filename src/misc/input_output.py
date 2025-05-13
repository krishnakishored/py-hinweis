def taking_input():
    # text  = input("Enter String: ")
    # print("Left justification",text.ljust(60,"*"))
    # print("Right justification",text.rjust(60,"*"))
    # print("Center justification",text.center(60,"*"))

    """accept list as a input from user"""
    # input_string = input("Enter a list element separated by space: ")
    # input_list = input_string.split()
    # print(input_list) # ['hello', '123', 'mic', 'testing']

    numbers = input("Calculating sum of element of input list: ").split()
    result = 0
    for num in numbers:
        result += int(num)
    print(result)


# https://www.python-course.eu/python3_formatted_output.php
def giving_output():
    """
    string modulo "%" is still available in Python3. You should get used to str.format() instead
    The general syntax for a format placeholder is %[flags][width][.precision]type
    """
    # format string % (string modulo operator)  Tuple with values
    print(
        "art:%5d,Price per Unit:%8.2f" % (453, 59.098)
    )  # art:  453,Price per Unit:   59.10
    print("%5.4x" % (47))  #  002f
    print("Only one percentage sign: %% " % ())

    print(
        "%#5X" % (47)
    )  # using flags - # : 	Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
    s = "Price: $ %8.2f" % (356.08977)
    print(s)

    # The pythonic way: the string method "format"
    """
    |  format(...)
    |      S.format(*args, **kwargs) -> str
    |
    |      Return a formatted version of S, using substitutions from args and kwargs.
    |      The substitutions are identified by braces ('{' and '}').
    |
    """
    print("First argument: {0}, second one: {1}".format(47, 11))
    print("Second argument: {1}, first one: {0}".format(47, 11))
    print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148))
    print("First argument: {}, second one: {}".format(47, 11))

    """ Using dictionaries in "format" """
    print(
        "The capital of {0:s} is {1:s}".format("Ontario", "Toronto")
    )  # We could have used empty curly braces

    print(
        "The capital of {province} is {capital}".format(
            province="Ontario", capital="Toronto"
        )
    )  # keyword parameters

    data = dict(province="Ontario", capital="Toronto")  # using a dictionary
    # The double "*" in front of data turns data automatically into the form 'province="Ontario",capital="Toronto"'.
    print("The capital of {province} is {capital}".format(**data))

    capital_country = {
        "United States": "Washington",
        "US": "Washington",
        "Canada": "Ottawa",
        "Germany": "Berlin",
        "France": "Paris",
        "England": "London",
        "UK": "London",
        "Switzerland": "Bern",
        "Austria": "Vienna",
        "Netherlands": "Amsterdam",
    }
    print("Countries and their capitals:")
    for c in capital_country:
        print(
            "{country}: {capital}".format(
                country=c, capital=capital_country[c]
            )
        )

    print("Countries and their capitals using a dictionary:")
    for c in capital_country:
        format_string = c + ": {" + c + "}"
        print(format_string.format(**capital_country))

    # Using Local Variable Names in "format"
    """
    "locals" is a function, which returns a dictionary with the current scope's local variables,
    i.e the local variable names are the keys of this dictionary and the corresponding values are the values of these variables
    
    >>> a = 42
    >>> b = 47
    >>> locals
        <built-in function locals>
    >>> locals()
        {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
         '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 42, 'b': 47}
       
    >>> print("{a},{b}".format(**locals())) # 42, 47
    """

    """
    The string class contains further methods,
    which can be used for formatting purposes as well: ljust, rjust, center and zfill
    """


def to_lowercase(input):
    return input.lower()


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


# https://realpython.com/python-f-strings/
def giving_output_fstrings():
    """
    f-strings are faster than both %-formatting and str.format().
    Python 3.6 introduces formatted string literals. They are prefixed with an 'f'.
    The formatting syntax is similar to the format strings accepted by str.format().
    Like the format string of format method, they contain replacement fields formed with curly braces.
    The replacement fields are expressions, which are evaluated at run time, and then formatted using the format() protocol.
    """
    price = 11.12
    print(f"Price in Euro: {price}")  # Price in Euro: 11.12
    name = "Eric"
    age = 74
    # 'F' can also be used instead of 'f'
    print(
        f"Hello {name}, you are age is {age}"
    )  # Hello Eric, you are age is 74

    """
    Because f-strings are evaluated at runtime,
    you can put any and all valid Python expressions in them
    """
    # a function is called
    print(f"{to_lowercase(name)} is funny")  # eric is funny

    new_comedian = Comedian("Eric", "Idle", "74")
    print(f"{new_comedian}")  # __str__(self) is invoked
    print(
        f"{new_comedian!r}"
    )  # __repr__(self) is called # Eric Idle is 74. Surprise!

    profession = "comedian"
    affiliation = "Monty Python"
    """You can have multiline strings: but place 'f' in each of the line """
    message = f"Hi {name}. You are a {profession}. You were in {affiliation}."
    print(message)

    """Fixed digits after decimal with f-strings"""
    a = 10.1023
    print(f"{a:.2f}")  # 10.10


if __name__ == "__main__":
    # taking_input()
    # giving_output()
    giving_output_fstrings()
