t = int(input())
for _ in range(t):
    s = int(input())
    result = ""

    # Start with 9, append it to the right most position, then decrement to 8, put it to the left of 9(if condition satisfies)
    # and so on
    i = 9
    while s:
        if i <= s:
            s -= i
            result = str(i) + result
        i -= 1

    print(result)
