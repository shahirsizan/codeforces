t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    # Check if it is possible to find integers x and y satisfying the constraints
    if 2 * l <= r:
        # Possible: x , y = l , 2*l
        print(l, 2*l)
    else:
        # Impossible
        print(-1, -1)
