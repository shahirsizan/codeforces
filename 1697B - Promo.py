n, q = map(int, input().split())
prices_list = list(map(int, input().split()))
sorted_prices_list = sorted(prices_list)
# Calculate prefix sum of sorted prices
# For example, if the list of prices is [2, 4, 6, 8, 10],
# the prefix sum list would be [0, 2, 6, 12, 20].
# Here, prefix_sum[i] represents the sum of prices from index `0 to i(exclusive)` in the list.
prefix_sum_list = [0]
for price in sorted_prices_list:
    prefix_sum_list.append(prefix_sum_list[-1] + price)

for _ in range(q):
    x, y = map(int, input().split())
    max_value_of_free_items = prefix_sum_list[n - x + y] - prefix_sum_list[n - x]
    print(max_value_of_free_items)



#_________________________________________________________
# THE FOLLOWING APPROACH YIELDS TIME EXCEEDED ERROR!

# for _ in range(q):
#     x, y = map(int, input().split())
#     purchased_list = prices_list[-x:]                   # Select the highest priced `x items`
#     max_value_of_free_items = sum(purchased_list[:y])   # Select the cheapest priced `y items` from `purchased_list` for free
#     print(max_value_of_free_items)

