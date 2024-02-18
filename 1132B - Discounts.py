# https://codeforces.com/problemset/problem/1132/B

n = int(input())
given_price_list = list(map(int, input().split()))
m = int(input())
coupon_list = list(map(int, input().split()))

sorted_list = sorted(given_price_list, reverse=True)   # In decreasing order
summ = sum(sorted_list)

for i in range(m):
    free_item_index = coupon_list[i] - 1
    net_summ = summ - sorted_list[free_item_index]
    print(net_summ)


