""" Homework 1
-- Due Sunday, September 11th at 23:59
-- Before starting, read
https://www.cis.upenn.edu/~cis192/homework/
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""


def fizzbuzz(n):
    """ If n is divisible by 3, return "Fizz"
    If n is divisible by 5, return "Buzz"
    If n is divisible by 3 and 5, return "FizzBuzz"
    Else, do nothing.
    """
    if n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        pass


def snapcrackle(n):
    """ If n is an int, return "Snap"
    If n is a float, return "Crackle"
    Else, do nothing.
    """
    if type(n) is int:
        return "Snap"
    elif type(n) is float:
        return "Crackle"
    else:
        pass


def is_prime(n):
    """ Return True if n is prime and False otherwise.
    Use this function to help write 'nth_prime' below.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            return True
    pass


def nth_prime(n):
    """ Return the nth prime number.
    """
    primes = []
    for x in range(100):
        if is_prime(x):
            primes.append(x)
    return primes[n]
    pass


def gcd_iter(n, m):
    """ An iterative function that calculates the GCD of n and m.
    Note that there is a function from the fractions module,
    fractions.gcd(a, b), that computes this -- do not use this
    function, but replicate its behavior exactly (including for
    negative or 0 inputs). See its documentation here:
    https://docs.python.org/3/library/fractions.html
    """
    while m:
        n, m = m, n % m
    return n 
    pass


def gcd_rec(n, m):
    """ A recursive function that calculates the GCD of n and m.
    """
    if m == 0:
        return n
    else:
        return gcd_rec(m, n % m)
    pass


def fib_iter(n):
    """ An iterative function that calculates the nth Fibonacci number.
    By convention, we'll say that the 1st Fibonacci number is 0
    and the 2nd Fibonacci number is 1.
    """
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b 
    return a 
    pass


def fib_rec(n):
    """ A recursive function that calculates the nth Fibonacci number.
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)
    pass


def main():
    pass


if __name__ == "__main__":
    """ Runs main() if we run this file with 'python3 hw1.py'. """
    main()
