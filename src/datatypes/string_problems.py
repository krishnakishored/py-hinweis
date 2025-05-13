# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    """
    i/p: this is a string
    o/p: this-is-a-string
    """

    # write your code here
    # result = line.split()
    # result = '-'.join(result) # print()
    return "-".join(line.split())


# https://www.hackerrank.com/challenges/whats-your-name/problem


def print_full_name(a, b):
    # Hello Ross Taylor! You just delved into python.
    print(f"Hello {a} {b}! You just delved into python.")


# https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    """abracadabra
    5 k
    o/p: abrackdabra
    """

    # l = list(string)
    # l[position] = character
    # return "".join(l)

    return string[:position] + character + string[position + 1 :]


# https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    # return s.title() # '12abcd'.title() results in '12Abcd' # Failure
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s


# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    # return string.count(sub_string) # works only for non-overlapping strings
    count = 0
    step = 0
    index = 0
    while index != -1:
        index = string.find(sub_string, step, len(string))
        step += index + len(sub_string)
        print(index)
        count += 1

    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
