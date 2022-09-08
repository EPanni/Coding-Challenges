""" fib
Write a function fib that takes in a number argument, n, and returns the n-th 
number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two 
numbers.

Solve this recursively.

test_00:
fib(0); # -> 0
"""

# Brute Force Solution
def fib_b_f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_b_f(n - 1) + fib_b_f(n - 2)


# Smart Solution
def fib(n):
    return _fib(n, {})


def _fib(n, memo):

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    a = fib(35)
    print(a)
