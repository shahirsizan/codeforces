# https://codeforces.com/problemset/problem/6/C

n = int(input())
times_list = list(map(int, input().split()))
a_i = 0
a_count = 0
b_i = n - 1
b_count = 0

prefix_time_a = 0
prefix_time_b = 0

while a_i <= b_i:
    if prefix_time_a <= prefix_time_b:
        a_count += 1
        prefix_time_a += times_list[a_i]
        a_i += 1
    else:
        b_count += 1
        prefix_time_b += times_list[b_i]
        b_i -= 1



print(a_count, b_count)
