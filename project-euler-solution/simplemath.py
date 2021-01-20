from math import sqrt

def isprime(x):
    if x <= 1: return False
    if x <= 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i+2) == 0:
            return False
        i += 6
    return True


def sieve(n):
    """generate all primes <= n"""
    a = [1] * (n + 1)
    a[0], a[1] = 0, 0
    for i in range(2, int(sqrt(n)) + 1):
        if a[i]:
            j = i * i
            while j <= n:
                a[j] = 0
                j += i
    return [i for i in range(n + 1) if a[i]]
