######################
# Required Questions #
######################

def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> def fn(x):
    ...     return x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    return [[x, fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]

#for x in seq:
        # if in bounds:
            # coords to list


def repeated(f, n):
    """Return the function that computes the nth application of f.
    >>> def increment(x):
    ...     return x + 1
    >>> def square(x):
    ...     return x**2
    >>> def triple(x):
    ...     return x*3
    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    "*** YOUR CODE HERE ***"
    k = f
    while n > 1:
        k = compose1(f, k)
        n -= 1
    return k



def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def double(f):
    """ Return a function that applies f twice.

    f -- a function that takes one argument

    >>> def square(x):
    ...     return x**2
    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    def repeat(x):
        return f(f(x))
    return repeat


def count_cond(condition, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(n):
        if (condition(n, i+1)):
            count += 1
    return count


def match_and_apply(pairs, function):
    """
    >>> pairs = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
    >>> def square(num):
    ...     return num**2
    >>> func = match_and_apply(pairs, square)
    >>> result = func(3)
    >>> result
    16
    >>> result = func(1)
    >>> result
    4
    >>> result = func(7)
    >>> result
    64
    >>> result = func(15)
    >>> print(result)
    None

    """
    "*** YOUR CODE HERE ***"
    def maa(x):
        for i in pairs:
            if i[0] == x:
                return function(i[1])
    return maa
