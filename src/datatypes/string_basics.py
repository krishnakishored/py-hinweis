# https://realpython.com/python-strings/#string-manipulation


def string_basics_1():
    s = "foo"
    t = "bar"
    u = "baz"
    print(s + t + u)  # foobarbaz
    """The * operator creates multiple copies of a string."""
    print(s * 4)  # foofoofoofoo
    # print('foo' * -8)  # ""   # empty string
    print(s in "That's food for thought.")  # True
    print("x" not in "That's food for thought.")  # True

    """
    Built-in String Functions
    chr()	Converts an integer to a character
    ord()	Converts a character to an integer
    len()	Returns the length of a string
    str()	Returns a string representation of an object
    """
    print(ord("a"), ord("A"), ord("0"))  # 97 65 48 # asii values
    # the ord() function will return numeric values for Unicode characters as well:
    print(ord("ß"), ord("€"))  # 223 8364
    print(chr(8364), chr(123))  # € { #  does the reverse of ord().

    print(str(49.2), str(3 + 4j))  # 49.2 (3+4j)

    v = "foobarbaz"
    # String indices can also be specified with negative numbers, -1 refers to the last character
    print(len(v), v[0], v[len(v) - 1], v[-1], v[-len(v)])  # 9 f z z f
    # String Slicing
    print(v[2:5])  # oba
    # slice indices must be integers '//' integer quotient
    print(v[: len(v) // 2] + v[len(v) // 2 :] == v)  # True
    print(v[-len(v) : -1])  # foobarba
    print(v[0 : len(v)])  # foobarbaz

    print(v[0:6:2])  # foa # slicing using step
    w = "12345" * 5
    """As with any slicing, the first and second indices can be omitted, 
    and default to the first and last characters respectively:"""
    print(w[::5])  # 11111
    print(w[4::5])  # 55555
    print(w[::-5])  # 55555
    """This is a common paradigm for reversing a string"""
    r = "If Comrade Napoleon says it, it must be right."
    print(r[::-1])  # .thgir eb tsum ti ,ti syas noelopaN edarmoC fI


def string_basics_2():
    """Strings are immuatable in Python"""
    s = "foobar"
    # s[3] = 'x' # 'str' object does not support item assignment
    # create a copy of the original string
    s = s[:3] + "X" + s[4:]
    print(s)  # fooXar
    print(s.replace("X", "P"))  # fooPar

    # case conversion on the target string
    s = "foO BaR BAZ quX"
    """capitalize() returns a copy of s with the first character converted to uppercase
     and all other characters converted to lowercase:"""
    print(s.capitalize())  # Foo bar baz qux
    print(s.lower())  # foo bar baz qux
    print("FOO Bar 123 baz qUX".upper())  # FOO BAR 123 BAZ QUX
    print("FOO Bar 123 baz qUX".swapcase())  # foo bAR 123 BAZ Qux
    """s.title() returns a copy of s in which the first letter of each word is converted to uppercase
    and remaining letters are lowercase:
    it does not handle apostrophes, possessives, or acronyms gracefully:
    """
    print("the sun also rises".title())  # The Sun Also Rises
    print(
        "what's happened to ted's IBM stock?".title()
    )  # What'S Happened To Ted'S Ibm Stock?

    """s.count(<sub>) returns the number of non-overlapping occurrences of substring <sub> in s:"""
    print("foo goo moo".count("oo"))  # 3
    print("foo goo moo".count("oo", 0, 8))  # 2
    print("ABCDCDC".count("CDC"))  # 1 # since only non-overlapping are counted

    print("foobar".endswith("bar"))  # True
    print("foobar".endswith("oob", 2, 4))  # False
    print("foobar".startswith("foo"))  # True
    print("foobar".startswith("bar", 3, 2))  # False
    """
    You can use .find() to see if a Python string contains a particular substring
    s.find(<sub>) returns the lowest index in s where substring <sub> is found
    """
    print("foo bar foo baz foo qux".find("foo"))  # 0
    print("foo bar foo baz foo qux".find("foo", 4, 7))  # -1 # not found
    """rfind(<sub>) returns the highest index in s where substring <sub> is found"""
    print("foo bar foo baz foo qux".rfind("foo"))  # 16
    # index() is similar to find() except it raises ValueError
    # print('foo bar foo baz foo qux'.index('grault')) # ValueError: substring not found
    # print('foo bar foo baz foo qux'.rindex('grault'))


def string_basics_3():
    """Methods in this group classify a string based on the characters it contains"""
    # print()
    print("abc123".isalnum())  # True
    print("abc123".isalpha())  # False
    print("123".isdigit())  # True
    print("foo$32".isidentifier())  # False
    print("foo32".isidentifier())  # True

    print(" \t \n ".isspace())  # True
    print("a\nb".isprintable())  # False
    """s.replace(<old>, <new>[, <count>])
    Replaces occurrences of a substring within a string.
    """
    print(
        "foo bar foo baz foo qux".replace("foo", "grault", 2)
    )  # grault bar grault baz foo qux

    """Converting Between Strings and Lists
    s.join(<iterable>)
    """
    print(", ".join(["foo", "bar", "baz", "qux"]))  # foo, bar, baz, qux
    print(list("corge"))  # ['c', 'o', 'r', 'g', 'e']
    print(":".join("corge"))  # c:o:r:g:e
    # print('---'.join(['foo', 23, 'bar'])) # TypeError: sequence item 1: expected str instance, int found
    print("---".join(["foo", str(23), "bar"]))  # foo---23---bar

    """ 
    s.partition(<sep>) splits s at the first occurrence of string <sep>.
    The return value is a three-part tuple
    """
    print("foo@@bar@@baz".partition("@@"))  # ('foo', '@@', 'bar@@baz')
    print("foo@@bar@@baz".rpartition("@@"))  # ('foo@@bar', '@@', 'baz')

    """
    s.split(sep=None, maxsplit=-1)
    s.rsplit(sep=None, maxsplit=-1)
    If the optional keyword parameter <maxsplit> is specified,
    a max of that many splits are performed, starting from the right end of s
    """
    print("foo\n\tbar   baz\r\fqux".rsplit())  # ['foo', 'bar', 'baz', 'qux']
    print("foo.bar.baz.qux".rsplit(sep="."))  # ['foo', 'bar', 'baz', 'qux']

    print(
        "www.realpython.com".rsplit(sep=".", maxsplit=1)
    )  # ['www.realpython', 'com']
    print(
        "www.realpython.com".split(".", maxsplit=1)
    )  # ['www', 'realpython.com']
    print(
        "foo\nbar\r\nbaz\fqux\u2028quux".splitlines()
    )  # ['foo', 'bar', 'baz', 'qux', 'quux']


def string_basics_4():
    """
    The bytes object is one of the core built-in types for manipulating binary data.
    A bytes object is an immutable sequence of single byte values.
    Each element in a bytes object is a small integer in the range 0 to 255.
    Only ASCII characters are allowed in a bytes literal.
    Any character value greater than 127 must be specified using an appropriate escape sequence:
    Many of the methods defined for string objects are valid for bytes objects as well:
    """
    b = b"foo bar baz"
    print(type(b), b)  # <class 'bytes'> b'foo bar baz'
    """bytes(<s>, <encoding>) - creates a bytes object from a string"""
    b = bytes("foo.bar", "utf8")
    print(b)  # b'foo.bar'

    print(bytes(8))  # b'\x00\x00\x00\x00\x00\x00\x00\x00'
    print(bytes([100, 102, 104, 106, 108]))  # b'dfhjl'
    """ Returns a bytes object constructed from a string of hexadecimal values."""
    b = bytes.fromhex(" aa 68 4682cc ")
    print(list(b))  # [170, 104, 70, 130, 204]
    """As opposed to .fromhex(), .hex() is an object method, not a class method. 
    Thus, it is invoked on an object of the bytes class, not on the class itself."""
    print(b.hex())  # aa684682cc

    """
    Python supports another binary sequence type called the bytearray.
    bytearray objects are very like bytes objects, despite some differences:
    There is no dedicated syntax built into Python for defining a bytearray literal, 
    like the 'b' prefix that may be used to define a bytes object. 
    A bytearray object is always created using the bytearray() built-in function:
    
    bytearray objects are mutable. You can modify the contents of a bytearray object using indexing and slicing:
    """
    ba = bytearray("foo.bar.baz", "UTF-8")
    print(ba)  # bytearray(b'foo.bar.baz')
    ba[5] = 0xEE
    print(ba)  # bytearray(b'foo.b\xeer.baz')
    print(bytearray(b"foo"))  # bytearray(b'foo')


if __name__ == "__main__":
    # string_basics_1()
    string_basics_2()
    # string_basics_3()
    # string_basics_4()
