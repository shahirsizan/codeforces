t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    if 2*a <= b:
        min_cost = (x + y) * a
    else:
        min_cost = min(x,y)*b + abs(x-y)*a

    print(min_cost)
