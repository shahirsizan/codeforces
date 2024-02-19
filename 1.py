# https://codeforces.com/problemset/problem/348/A
# sol: https://codeforces.com/problemset/status/348/problem/A/page/2?order=BY_PROGRAM_LENGTH_ASC

from math import ceil

n = int(input())
given_array = list(map(int, input().split()))
rounds_needed = max( max(given_array), ceil(sum(given_array)/(n-1)) )

print(rounds_needed)
