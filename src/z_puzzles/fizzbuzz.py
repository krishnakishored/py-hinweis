"""
3,5 - fizzBuzz
only 3 - Fizz
only 5 - Buzz
none of 3, 5 - i
"""


def fizzBuzz(n):
    for i in range(1, n + 1):
        result = ""  #
        if i % 3 == 0:
            result = result + "Fizz"
        if i % 5 == 0:
            result = result + "Buzz"

        if not result:
            result = i
        print(result)


def fizzBuzzExtended(n, rules):
    """
    Print numbers from 1 to n, substituting strings based on divisibility rules.

    Args:
        n (int): Upper limit of the sequence.
        rules (List[Tuple[int, str]]): List of (divisor, word) rules.

    Returns:
        List[str]: Resulting sequence.
    """
    result = []
    for i in range(1, n + 1):
        output = ""
        for divisor, word in rules:
            if i % divisor == 0:
                output += word
        if not output:
            output = str(i)
        result.append(output)
    print(" ".join(result))
    return result


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    fizzBuzz(n)
    # Example usage
    fizzBuzzExtended(15, [(3, "Fizz"), (5, "Buzz")])
