t = int(input())
for _ in range(t):
    n = int(input())
    plays_list = [0] * n
    clears_list = [0] * n
    ans = True

    for i in range(n):
        plays_list[i], clears_list[i] = map( int, input().split() )

    if plays_list[0] < clears_list[0]:
        print('NO')
        continue

    for i in range(1, n):
        if plays_list[i] < plays_list[i-1] \
                or clears_list[i] < clears_list[i-1] \
                or plays_list[i] < clears_list[i] \
                or ( clears_list[i] - clears_list[i-1] ) > ( plays_list[i] - plays_list[i-1] ):
            ans = False
            break

    if ans:
        print('YES')
    else:
        print('NO')
