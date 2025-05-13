def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    print("result: ", old)
    return old


def rfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rfib(n - 1) + rfib(n - 2)
