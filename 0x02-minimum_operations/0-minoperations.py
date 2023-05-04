#!/usr/bin/python3

def minOperations(n):

    if n == 1:

        return 0

    x = 1

    ans = float('inf')

    while x <= n:

        if n % x == 0:

            ans = min(ans, n//x - 1)

        x *= 2

    if ans != float('inf'):

        return ans

    for x in range(n//2, 0, -1):

        if n % x == 0:

            f = n // x

            ans = min(ans, f*x//f - x + minOperations(f))

    if ans != float('inf'):

        return ans

    return 0

