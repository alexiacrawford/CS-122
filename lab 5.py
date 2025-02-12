import doctest


def foo(x):
    '''
    (x: int) -> int

    add 1 to x and return new value

    >>> foo(4)
    5
    >>> foo(10)
    11
    >>> foo(0)
    1
    >>> foo(-10)
    -9
    '''
    return x+1

doctest.testmod()

print(doctest.testmod())
