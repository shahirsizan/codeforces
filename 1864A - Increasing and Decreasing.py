t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())

    if y-x < n*(n-1)/2:     # the sum of the sequence (1+2+…+(n−1)+n) can be calculated by the formula `n*(n-1)/2`.
        print(-1)           # if `y−x` is less than `n*(n-1)/2`, there is not enough space to accommodate the strictly increasing array.
    else:

        result_list = [0] * n
        result_list[0] = x
        result_list[n-1] = y
        j = 1

        for i in range(n-2, 0, -1):     # we iterate backwards
            result_list[i] = result_list[i+1] - j
            j += 1

        print(*result_list)
