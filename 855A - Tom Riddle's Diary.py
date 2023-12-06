# https://codeforces.com/problemset/problem/855/A

t = int(input())
unique_names = set()

for _ in range(t):
    name = input().strip()
    if name not in unique_names:
        print("NO")
        unique_names.add(name)
    else:
        print("YES")
