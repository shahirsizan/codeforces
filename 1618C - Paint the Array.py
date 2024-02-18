# https://codeforces.com/problemset/problem/1618/C

import math
from functools import reduce

t = int(input())
for _ in range(t):
    n = int(input())
    given_array = list(map(int, input().split()[:n]))
    even_indexed_elements = list()
    odd_indexed_elements = list()

    for i in range(n):
        if i % 2 == 0:
            even_indexed_elements.append(given_array[i])
        else:
            odd_indexed_elements.append(given_array[i])

    gcd_of_evens = reduce(math.gcd, even_indexed_elements)
    gcd_of_odds = reduce(math.gcd, odd_indexed_elements)

    redflag_of_evens = 0
    redflag_of_odds = 0

    if gcd_of_evens == gcd_of_odds:
        print(0)
        continue

    for i in range(n):
        # Check if at least one of the `odd-indexed-elements` is divisible by the `gcd_of_even_indices`
        # or if at least one of the `even-indexed-elements` is divisible by `gcd_of_odd_indices`
        # if any of them yields true, that means there are some instances where
        # coloring two adjacent cells differently will not be possible. Print `0`
        if i % 2 == 0 and (given_array[i] % gcd_of_odds == 0):
            redflag_of_odds = 1
        if i % 2 != 0 and (given_array[i] % gcd_of_evens == 0):
            redflag_of_evens = 1

    if redflag_of_evens == 0:
        print(gcd_of_evens)
    elif redflag_of_odds == 0:
        print(gcd_of_odds)
    elif redflag_of_evens == 1 and redflag_of_odds == 1:
        print(0)
