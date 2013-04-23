# Find the largest palindrome made from the product of two 3-digit numbers.
# as product of 3 digit is either 5 digit or 6 digit, better try the 6 digit.
# aslo 6 digit palindrome is div by 11, so try that way.


def isPlindrome(num):
    numstr = str(num)
    rever = numstr[::-1]
    if rever == numstr:
        return True
    else:
        return False


def biggerwins(x, y):
    if x > y:
        return x
    else:
        return y

result = []  # the result stack

for fst in range(990, 100, -11):    # have to be div by 11
    for snd in range(999, 100, -1):
        prod = fst * snd
        if (isPlindrome(prod)):
            result.append(prod)
            # the biggest inner round found, skip to next 11*n
            break

print(reduce(biggerwins, result))
