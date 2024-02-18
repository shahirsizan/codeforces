# https://codeforces.com/problemset/problem/1411/B


def is_fair(original_number):
    duplicate_number = original_number
    while duplicate_number:
        digit = duplicate_number % 10
        if (digit != 0) and (original_number % digit != 0):
            return False
        duplicate_number = duplicate_number // 10
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while not is_fair(n):
        n += 1
    print(n)
