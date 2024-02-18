# https://codeforces.com/problemset/problem/1840/B
import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if math.log2(n) >= k:
        print(2**k)
    else:
        print(n+1)
