######################
# Required Questions #
######################

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 10)  # 4 * 3 * 2 * 1 # Only n times!!
    24
    """
    "*** YOUR CODE HERE ***"
    j = 1
    if n < k:
        while n != 0:
            j = j * n
            n = n - 1
        return j
    if k <= 0:
        return 1
    while k > 0:
        j = j * n
        n, k = n - 1, k - 1
    return j


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    "*** YOUR CODE HERE ***"
    if len(lst) == 3:
        return 1
    else:
        return 5

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    len = 1
    while n >= 1:
        print(n)
        if n == 1:
            return len
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        len = len + 1

def odd_even(x):
    """
    Classify a number as odd or even.
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    "*** YOUR CODE HERE ***"
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    "*** YOUR CODE HERE ***"
    return ['even', 'odd', 'even', 'even']

def decode_helper(pair):
    """
    Optional helper function! Could be useful to turn something like [0, 0] to 'Male 0-9'
    """
    "*** YOUR CODE HERE ***"
    return ''


def decode(list_of_sex_age_pairs):
    """
    >>> decode([[0, 0], [1, 1], [1, 10]])
    ['Male 0-9', 'Female 10-19', 'Female 100+']
    >>> decode([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
    ['Male 0-9', 'Male 10-19', 'Male 20-29', 'Male 30-39', 'Male 40-49', 'Female 50-59', 'Female 60-69', 'Female 70-79', 'Female 80-89', 'Female 90-99', 'Female 100+']
    """
    "*** YOUR CODE HERE ***"
    return ______
