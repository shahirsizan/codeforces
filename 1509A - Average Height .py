def solve(n, heights):
    even = [h for h in heights if h % 2 == 0]
    odd = [h for h in heights if h % 2 != 0]
    arranged = even + odd
    return arranged


t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))

    arranged_heights = solve(n, heights)
    print(*arranged_heights)

'''
Sum of two even numbers is even
Sum of two odd numbers is even
So, an `all even then all odd` or `all odd then all even` sequence would yield max number of integers averages.
'''
