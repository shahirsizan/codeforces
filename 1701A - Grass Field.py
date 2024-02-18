t = int(input())
for t in range(t):
    a , b = map(int, input().split())
    c , d = map(int, input().split())
    if (a == b == c == d == 0):
        print(0)
    elif (a == b == c == d == 1):
        print(2)
    else:
        print(1)