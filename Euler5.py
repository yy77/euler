# the smallest positive number that is evenly divisible by 1 to 20

from functools import reduce

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


print(reduce(lcm, range(1, 20)))
