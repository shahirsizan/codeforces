# https://codeforces.com/problemset/problem/1213/B

t = int(input())
for _ in range(t):
    n = int(input())
    prices_list = list(map(int, input().split()[:n]))

    bad_days_count = 0
    min_price = prices_list[-1]

    # we'll iterate through the list from the RHS.
    for i in range(n-2, -1, -1):
        if prices_list[i] > min_price:
            bad_days_count += 1
        min_price = min(prices_list[i], min_price)

    print(bad_days_count)
