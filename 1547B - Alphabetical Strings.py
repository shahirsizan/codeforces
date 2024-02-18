t = int(input())

for _ in range(t):
    s = input().strip()
    i = 0
    j = len(s)

    while j > 0 and chr(96 + j) in (s[i], s[i + j - 1]):
        i += chr(96 + j) == s[i]
        j -= 1

    if j > 0:
        print("NO")
    else:
        print("YES")
