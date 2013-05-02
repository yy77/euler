# get the 10,001st prime number
import collections
from itertools import islice

def take_nth(n,iterable):
    return islice(iterable, n-1, n).next()


def genPrime():
    D = collections.defaultdict(lambda :[])
    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D[p+q].append(p)
            del D[q]
        q += 1

print(take_nth(10001, genPrime()))
