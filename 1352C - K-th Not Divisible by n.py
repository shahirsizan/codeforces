#   https://codeforces.com/problemset/problem/1352/C


def is_kth_non_divisible(n, k, x):
    return x - (x // n) >= k

def find_kth_non_divisible(n, k):
    left, right = 1, n * k

    while left < right:
        mid = (left + right) // 2
        if is_kth_non_divisible(n, k, mid):
            right = mid
        else:
            left = mid + 1

    return left

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    result = find_kth_non_divisible(n, k)
    print(result)
