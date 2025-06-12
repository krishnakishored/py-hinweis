def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def y_intercept(x1, y1, x2, y2):
    # to find y-intercept.
    m = slope(x1, y1, x2, y2)
    c = y1 - (m * x1)
    # print('y-intercept:')
    return c


def findTheclosestElement(array, target):
    res = min(enumerate(array), key=lambda x: abs(target - x[1]))
    return res  # (index, value)


def findPrice(m, x, c):
    # y = mx + c
    return (m * x) + c


def interpolate(n, instances, prices):
    """
    n - needed no.of instances
    m - size of array instances, prices


    1. num_instances is exactly - same unit price
    2.  between large and small
    3.  beyond

    []
    [(25,5.0),(50,4.0),(100,3.0)] - (tuples of instances, price) - x,y coordinates

    """
    result_price = 0  # to be returned
    (index, elem) = findTheclosestElement(instances, n)
    print(index, elem)

    if instances[index] == n:
        return str(prices[index])  # exact_match

    elif index < len(instances) - 1 and index >= 0:
        # get
        x1 = float(instances[index])
        y1 = float(prices[index])
        x2 = float(instances[index + 1])
        y2 = float(prices[index + 1])
        m = slope(x1, y1, x2, y2)
        c = y_intercept(x1, y1, x2, y2)
        result_price = findPrice(m, int(n), c)

    elif index == len(instances) - 1:
        x1 = float(instances[index - 1])
        y1 = float(prices[index - 1])
        x2 = float(instances[index])
        y2 = float(prices[index])
        m = slope(x1, y1, x2, y2)
        c = y_intercept(x1, y1, x2, y2)
        result_price = findPrice(m, int(n), c)

    return str(result_price)

    # pass
    # line-->  y = mx + c


if __name__ == "__main__":
    # fizzBuzz(31)
    # interpolate()
    array = [10, 25, 50, 100, 500]
    prices = [2.46, 2.58, 2.0, 2.25, 3.0]
    # print(findTheclosest(array,51))
    n = 5
    print(interpolate(n, array, prices))
