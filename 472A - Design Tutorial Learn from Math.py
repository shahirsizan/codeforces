def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_composite_pair(n):
    for i in range(4, n):
        if not is_prime(i) and not is_prime(n - i):
            return i, n - i

n = int(input())
x, y = find_composite_pair(n)
print(x, y)
