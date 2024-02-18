for _ in range(int(input())):
    k = int(input())
    s = input().strip()
    count = 0

    for i in range(0, k-2):
        # If characters at index `i` and `i+2` both are the same
        # that means, in both the first and the second turn
        # where we'll delete string[i] and string[i+2]
        # we'll get the same unique string. So, we cant increase `count`
        if s[i] == s[i + 2]:
            continue
        else:
            count += 1

    print(count + 1)
