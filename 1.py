# https://codeforces.com/problemset/problem/1132/B

n = int(input())
given_price_list = list(map(int, input().split()))
m = int(input())
coupon_list = list(map(int, input().split()))

for i in range(m):
    copy_given_price_list = given_price_list
    sorted_list = sorted(copy_given_price_list, reverse=True)   # In decreasing order

    copy_given_price_list = sorted_list[:(n - coupon_list[i])] + sorted_list[(n - coupon_list[i] + 1):]
    total_cost_after_coupon = sum(copy_given_price_list)
    print(                        total_cost_after_coupon    )


