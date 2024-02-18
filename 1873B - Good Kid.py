# https://codeforces.com/problemset/problem/1873/B

t = int(input())
for _ in range(t):
    n = int(input())
    digits = list( map(int, input().split()) )

    # just find the smallest digit and add 1 to it.
    min_digit = min(digits)
    min_digit_index = digits.index(min_digit)
    digits[min_digit_index] += 1

    product = 1
    for digit in digits:
        product *= digit

    print(product)
