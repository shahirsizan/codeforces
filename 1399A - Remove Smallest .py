t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()[:n]))
    a.sort()

    possible = all( abs(a[i] - a[i-1]) <= 1 for i in range(1, n) )

    if possible:
        print("YES")
    else:
        print("NO")
