# https://codeforces.com/problemset/problem/401/C

no_of_zeros, no_of_ones = map( int, input().split() )

if no_of_ones > (2*no_of_zeros)+2 or no_of_zeros > no_of_ones+1:
    print(-1)
else:
    if no_of_zeros <= no_of_ones <= 2*no_of_zeros:
        print('110' * (no_of_ones - no_of_zeros) + '10' * (2 * no_of_zeros - no_of_ones))
    elif no_of_ones > 2 * no_of_zeros:
        print('110' * no_of_zeros + '1' * (no_of_ones - 2 * no_of_zeros))
    else:
        print('01' * no_of_ones + '0')
