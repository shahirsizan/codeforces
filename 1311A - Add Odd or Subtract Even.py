t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    diff = b - a

    if diff == 0:                           # ex: a = 10 and b = 10
        moves = 0
    elif diff > 0 and diff % 2 == 0:        # ex: a = 4 and b = 10
        moves = 2
    elif diff > 0 and diff % 2 == 1:        # ex: a = 5 and b = 10
        moves = 1
    elif diff < 0 and abs(diff) % 2 == 0:   # ex: a = 10 and b = 4
        moves = 1
    elif diff < 0 and abs(diff) % 2 == 1:   # ex: a = 10 and b = 5
        moves = 2

    print(moves)
