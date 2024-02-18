# https://codeforces.com/problemset/problem/1294/A

t = int(input())
for _ in range(t):
    a, b, c, n = map( int, input().split() )

    total_coins = a + b + c + n

    if ( total_coins%3 == 0 ) and ( max(a, b, c) <= total_coins//3 ):
        print("YES")
    else:
        print("NO")
