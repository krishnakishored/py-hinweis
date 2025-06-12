# Detect Floating Point Numbers
# Description: Given multiple strings, determine which ones represent valid floating-point numbers.

# Skills Tested: Regular expressions, string parsing, input/output handling.

# Example:
# Input: 4, followed by 4.0O0, -1.00, +4.54, SomeRandomStuff
# Output:

# text
# False
# True
# True
# False


def is_floating_point_number(s):
    """
    Check if the input string s is a valid floating-point number.

    :param s: Input string to check
    :return: True if s is a valid floating-point number, False otherwise
    """
    # Skip empty strings
    if not s:
        return False

    # Track if we've seen decimal point and if number is valid
    seen_decimal = False
    seen_digit = False
    i = 0

    # Check for sign
    if i < len(s) and s[i] in ["+", "-"]:
        i += 1

    # Process remaining characters
    while i < len(s):
        char = s[i]

        # Handle decimal point
        if char == ".":
            if seen_decimal:  # Multiple decimal points not allowed
                return False
            seen_decimal = True

        # Handle digits
        elif char.isdigit():
            seen_digit = True

        # Invalid character
        else:
            return False

        i += 1

    # Must have at least one digit
    return seen_digit

    # regex solution

    #     import re
    #     pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'
    #     return bool(re.match(pattern, s))


if __name__ == "__main__":
    import sys

    # Read the number of test cases
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        # Read each string and check if it's a floating-point number
        s = sys.stdin.readline().strip()
        print(is_floating_point_number(s))
# Example usage:
