def find_s(n):
    if n == 1:
        return -1
    else:
        return int("2" + "3" * (n - 1))

t = int(input())
for _ in range(t):
    n = int(input())
    result = find_s(n)
    print(result)
