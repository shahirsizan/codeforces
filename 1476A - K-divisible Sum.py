import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    b = b * math.ceil(a / b)
    result = math.ceil(b / a)

    print(result)
