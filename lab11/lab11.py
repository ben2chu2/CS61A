#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = start

    def __next__(self):
        count = 0
        if self.start == self.end + 1:
            self.start = self.next
            raise StopIteration
        if self.start <= self.end:
            count = self.start
            self.start += 1
        return count

    def __iter__(self):
        return self


# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, string):
        self.string = string
        self.len = len(string)
        self.index = 0

    def __next__(self):
        if self.index >= self.len:
            raise StopIteration
        else:
            result = self.string[self.index]
            self.index += 1
            return result

    def __iter__(self):
        return self

##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    num = n
    while num >= 0:
        yield num
        num -= 1

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, n):
        self.start = n

    def __next__(self):
        if self.start <= -1:
            raise StopIteration
        else:
            result = self.start
            self.start -= 1
            return result

    def __iter__(self):
        return self

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
    yield 1
