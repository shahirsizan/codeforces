# https://codeforces.com/problemset/problem/696/A

n = int(input())
passing_fees_dict = dict()

def update_passing_fee(start, end, increment):
    while start != end:
        if start < end:
            start, end = end, start
        passing_fees_dict[start] = passing_fees_dict.get(start, 0) + increment
        start //= 2

def find_total_fee(start, end):
    total_fee = 0
    while start != end:
        if start < end:
            start, end = end, start
        passing_fees_dict[start] = passing_fees_dict.get(start, 0)
        total_fee += passing_fees_dict[start]
        start //= 2
    return total_fee

for i in range(n):
    events_list = list(map(int, input().split()))

    if events_list[0] == 1:     # Governments turn
        update_passing_fee(events_list[1], events_list[2], events_list[3])

    else:                       # Barneys turn
        sum_of_passing_fee = find_total_fee(events_list[1], events_list[2])
        print(sum_of_passing_fee)
