# https://codeforces.com/problemset/problem/1807/D

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    given_list = list(map(int, input().split()))
    prefix_sum = [0] * (n+1)

    for i in range(n):
        prefix_sum[i+1] = given_list[i] + prefix_sum[i]

    for _ in range(q):
        left, right, k = map(int, input().split())

        new_sum = (  prefix_sum[n] - (prefix_sum[right]-prefix_sum[left-1])  ) + (  (right-left+1) * k  )

        if new_sum % 2 == 1:
            print("YES")
        else:
            print("NO")
