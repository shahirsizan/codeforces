n, min_variation, max_variation = map(int, input().split())
min_array = [0] * n
max_array = [0] * n
base_value = 2 ** (max_variation-1)

for i in range(n):      # to generate array that has the most number of 1 so that sum is minimum
    if i <= (n-min_variation):
        min_array[i] = 1
    else:
        min_array[i] = min_array[i-1] * 2

for i in range(n):      # to generate array that has the most number of variations so that sum is maximum
    if i <= (n-max_variation):
        max_array[i] = base_value
    else:
        max_array[i] = max_array[i-1] // 2

print(sum(min_array), sum(max_array))
