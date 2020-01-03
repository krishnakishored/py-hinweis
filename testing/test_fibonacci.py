import pytest
from fibonacci import fib, rfib

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(34) == 5702887



@pytest.mark.crazy
@pytest.mark.slow
def test_rfib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert rfib(34) == 5702887

@pytest.mark.parametrize(
    'n, res', [(0, 0), 
               (1, 1), 
               (2, 1),
               (3, 2), 
               (4, 3),
               (5, 5),
               (6, 8)])
def test_fib_2(n, res):
    assert fib(n) == res


results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 
           34, 55, 89, 144, 233, 377]


def test_fib_3(cmdopt):
    if cmdopt == "full":
        num = len(results)
    else:
        num = len(results)
        if int(cmdopt) < len(results):
            num = int(cmdopt)
    for i in range(num):
        assert fib(i) == results[i]