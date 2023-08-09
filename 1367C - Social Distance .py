t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    # Binary string `s`
    s = "0"*k + input()[:n] + "0"*k
    # Split `s` where a `1` is encountered to get segments of consecutive zeros
    segments_list = s.split("1")

    count = 0
    for list in segments_list:
        count += max( (len(list) - k) // (k + 1), 0 )

    print(count)
