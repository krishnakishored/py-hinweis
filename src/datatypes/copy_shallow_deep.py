# https://python-course.eu/python3_deep_copy.php
# https://www.programiz.com/python-programming/shallow-deep-copy
# https://realpython.com/copying-python-objects/

"""
Python creates only real copies, if it has to,
i.e. if the user, the programmer, explicitly demands it.
"""


def using_id_function():
    x = 3
    y = x  # y points to the same memory location as X.
    print(id(x), id(y))  # 1503920656 1503920656
    # But unlike "real" pointers like those in C and C++, things change,
    # when we assign a new value to y
    y = 4
    print(id(x), id(y))  # 1503920656 1503920688
    print(x, y)  # 3 4


def copying_a_list():
    colours1 = ["red", "blue"]
    colours2 = colours1
    print(colours2)  # ['red', 'blue']
    print(id(colours1), id(colours2))  # 45079752 45079752

    colours2 = ["rouge", "vert"]
    print(colours1)
    print(colours2)
    # ['red', 'blue']
    # ['rouge', 'vert']

    print(id(colours1), id(colours2))
    # 45079752 45115976

    # Copy with the Slice Operatorl
    print("Copy with the Slice Operator")
    list1 = ["a", "b", "c", "d"]
    list2 = list1[:]
    print(id(list1), ": ", "list1 items:")
    print(id(list2), ": ", "list2 items:")

    for item1 in list1:
        print(
            id(item1), " ", end=""
        )  # 4564504504  4563857280  4563807848  4563998960
    print("----------------------------")
    for item2 in list2:
        print(id(item2), " ", end="")
    print(
        "----------------------------"
    )  # 4564504504  4563857280  4563807848  4563998960

    list2[0] = "z"  # only id of first element changes
    for item1 in list1:
        print(
            id(item1), " ", end=""
        )  # 4564504504  4563857280  4563807848  4563998960
    print("----------------------------")
    for item2 in list2:
        print(
            id(item2), " ", end=""
        )  # 4564763624  4563857280  4563807848  4563998960
    print("----------------------------")

    # for sublists
    lst1 = ["a", "b", ["ab", "ba"]]
    lst2 = lst1[:]
    for item1 in lst1:
        print(
            id(item1), " ", end=""
        )  # 4514586552  4513939328  4514808584  ----------------------------
    print("----------------------------")
    for item2 in lst2:
        print(
            id(item2), " ", end=""
        )  # 4514586552  4513939328  4514808584  ----------------------------
    print("----------------------------")

    print(lst1[2][1], "__", lst2[2][1])  # ba __ ba
    lst2[2][1] = "d"
    # We can see that both lst1 and lst2 are affected by the assignment lst2[2][1] = 'd':
    print(id(lst1[2][1]), ": ", "lst1[2][1] items:")
    print(id(lst2[2][1]), ": ", "lst2[2][1] items:")
    print(lst1[2][1], "__", lst2[2][1])  # d __ d


"""
# Using the Method deepcopy from the Module copy
A solution to the described problems provide the module "copy".
This module provides the method "deepcopy", which allows a complete or deep copy of an arbitrary list, i.e. shallow and other lists.
"""


def using_deepcopy():
    from copy import deepcopy

    lst1 = ["a", "b", ["ab", "ba"]]
    lst2 = deepcopy(lst1)
    print(id(lst1), ": ", "lst1 items:")  # 4464694408 :  lst1 items:
    print(id(lst2), ": ", "lst2 items:")  # 4464693448 :  lst2 items:
    """ 
    Though sublists are copied. An interesting fact is that the strings are not copied:
     lst1[0] and lst2[0] reference the same string.
    """
    print(
        id(lst1[0]), id(lst1[1]), id(lst1[2]), id(lst1[2][1])
    )  # 4456878008 4456230784 4457104392 4457137520
    print(
        id(lst2[0]), id(lst2[1]), id(lst2[2]), id(lst2[2][1])
    )  # 4456878008 4456230784 4456814024 4457137520


def copy_summary():
    import copy

    old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    new_list_1 = copy.copy(old_list)
    new_list_2 = copy.deepcopy(old_list)

    old_list.append([4, 4, 4])
    print(
        "Old list:", old_list
    )  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [4, 4, 4]]
    print("shallow list:", new_list_1)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("deep list:", new_list_2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    old_list[1][1] = "AA"
    print(
        "Old list:", old_list
    )  # [[1, 2, 3], [4, 'AA', 6], [7, 8, 9], [4, 4, 4]]
    print("shallow list:", new_list_1)  # [[1, 2, 3], [4, 'AA', 6], [7, 8, 9]]
    print("deep list:", new_list_2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


"""Copying Arbitrary Python Objects"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """using __repr__() we can easily inspect objects created from this class in the Python interpreter"""
        return f"Point({self.x!r},{self.y!r})"
        # return 'Point(%r, %r)' % (self.x, self.y) # without using f-string


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f"Rectangle({self.topleft!r},{self.bottomright!r})"


def copy_arbitrary_py_obj():
    import copy

    a = Point(23, 42)
    b = copy.copy(a)
    # Because our point object uses immutable types (ints) for its coordinates,
    # there’s no difference between a shallow and a deep copy in this case.
    print(a)  # Point(23,42)
    print(b)  # Point(23,42)

    rect = Rectangle(Point(0, 1), Point(5, 6))
    srect = copy.copy(rect)
    print(rect)
    print(srect)

    # modify an object deeper in the object hierarchy,
    # and then you’ll see this change reflected in the (shallow) copy as well
    rect.topleft.x = 999
    print(rect)  # Rectangle(Point(999,1),Point(5,6))
    print(srect)  # Rectangle(Point(999,1),Point(5,6))

    drect = copy.deepcopy(srect)
    drect.topleft.x = 222
    print(drect)  # Rectangle(Point(222,1),Point(5,6))
    print(srect)  # Rectangle(Point(999,1),Point(5,6))


if __name__ == "__main__":
    # using_id_function()
    # copying_a_list()
    # using_deepcopy()
    # copy_summary()
    copy_arbitrary_py_obj()
