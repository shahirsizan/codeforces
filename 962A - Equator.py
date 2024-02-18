# https://codeforces.com/problemset/problem/962/A
# sol - https://codeforces.com/problemset/status/962/problem/A/page/4?order=BY_PROGRAM_LENGTH_ASC

import math

n = int(input())
problems_list = list(map(int, input().split()))
total_problems = sum(problems_list)

# Calculate the prefix sums
prefix_sums_list = [0] * (n + 1)


for i in range(1, n+1):
    prefix_sums_list[i] = problems_list[i - 1] + prefix_sums_list[i - 1]


target_problems = math.ceil(total_problems / 2)
if n == 1:
    equator_index = 1
else:
    #equator_index = prefix_sums_list.index(target_problems)
    for i in range(len(prefix_sums_list)):
        if prefix_sums_list[i] >= target_problems:
            equator_index = i
            break



print(equator_index)
