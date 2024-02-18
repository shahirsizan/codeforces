# https://codeforces.com/problemset/problem/1542/A

t = int(input())
for _ in range(t):
    n = int(input())

    numbers = list( map(int, input().split()) )
    odd_count = even_count = 0
    for num in numbers:
        if num%2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if odd_count == even_count:
        print("Yes")
    else:
        print("No")
