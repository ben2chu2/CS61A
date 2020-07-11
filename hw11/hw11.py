def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for i in s:
        yield i * k

class Scale:
    def __init__(self, s, k):
        self.set = s
        self.scaled = k
        self.start = 0

    def __next__(self):
        if self.start >= len(self.set):
            raise StopIteration
        else:
            result = self.set[self.start] * self.scaled
            self.start += 1
            return result

    def __iter__(self):
        return self



def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1 and
    make sure to remove the repeated values in both.
    You can also assume that s0 and s1 represent infinite sequences.

    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    "*** YOUR CODE HERE ***"
    while True:
        if e0 == e1:
            yield e0
            e0 = next(i0)
            e1 = next(i1)
        elif e0 < e1:
            yield e0
            e0 = next(i0)
        else:
            yield e1
            e1 = next(i1)

class Merge:
    def __init__(self, s0, s1):
        self.itr1 = s0
        self.itr2 = s1
        self.start = 0
        self.sorted = sorted(s0 + s1)

    def __next__(self):
        if self.start >= len(sorted):
            raise StopIteration
        else:
            result = self.sorted[self.start]
            self.start += 1
            return result

    def __iter__(self):
        return self



def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def multiple():
        i = 0
        while i <= m - 1:
            yield filter(lambda x: x % m == i, remainders_nat())
            i += 1

    return multiple()

def remainders_nat():
    i = 0
    while True:
        yield i
        i += 1


from math import sqrt

def is_prime(n):
    """
    Return True if n is prime, false otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(19)
    True
    """
    "*** YOUR CODE HERE ***"
    i = 2
    if n == 1:
        return False
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes():
    """
    An infinite generator that outputs primes.

    >>> p = primes()
    >>> for i in range(3):
    ...     print(next(p))
    ...
    2
    3
    5
    """
    "*** YOUR CODE HERE ***"
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1



# the naturals generator is used for testing scale and merge functions
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1
