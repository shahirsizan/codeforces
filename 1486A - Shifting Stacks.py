# https://codeforces.com/problemset/problem/1486/A

t = int(input())
for _ in range(t):
    i = 0
    j = 0
    res = True

    n = int(input())
    stack_heights = list(map(int, input().split()))

    for k in range(n):
        i += k
        j += stack_heights[k]
        if j < i:
            res = False

    if res == False:
        print("NO")
    else:
        print("YES")

