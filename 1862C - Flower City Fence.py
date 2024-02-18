# https://codeforces.com/problemset/problem/1862/C

t = int(input())
for _ in range(t):
    n = int(input())
    heights_list = list(map(int, input().split()[:n]))
    inversed_heights_list = [0] * (n+1)   # (n+1) required, because in the last step, we have to add the heights from the RHS of the list.

    if heights_list[0] != n:
        print("NO")
        continue

    for i in range(0, n):
        inversed_heights_list[heights_list[i]-1] += 1

    for i in range(n-1, -1, -1):
        inversed_heights_list[i] += inversed_heights_list[i+1]

    if inversed_heights_list[:n] == heights_list:
        print("YES")
    else:
        print("NO")
