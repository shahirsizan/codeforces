t = int(input())

for _ in range(t):
    x = int(input())
    # Print a pair of positive integers a and b such that `GCD(a, b) + LCM(a, b) = x`
    # One possible solution is (x-1, 1)
    print(x - 1, 1)
