# https://codeforces.com/problemset/problem/1064/A

a, b, c = sorted( map(int, input().split()) )

if a + b > c:
    print(0)
else:
    additional_minutes_required = c - (a + b) + 1
    print(additional_minutes_required)
