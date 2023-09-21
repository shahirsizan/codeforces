t = int(input())

for _ in range(t):
    n = int(input())
    whiteBoardSequence = list(map(int, input().split()[:n]))

    result = []
    i = 0
    j = n - 1

    while i <= j:
        if i == j:
            result.append(whiteBoardSequence[i])
        else:
            result.append(whiteBoardSequence[i])
            result.append(whiteBoardSequence[j])
        i += 1
        j -= 1

    print(" ".join(map(str, result)))
