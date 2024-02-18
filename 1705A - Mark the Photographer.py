t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    heights_list = sorted(map(int, input().split()))

    result = all( [ heights_list[i]+x <= heights_list[n+i] for i in range(n) ] )

    print("YES" if result else "NO")
