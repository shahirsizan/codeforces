t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # Answer is equal to m multiplied by the minimum of (n-1) and 2
    result = m * min(n - 1, 2)
    print(result)
