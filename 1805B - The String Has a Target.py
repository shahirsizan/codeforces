# https://codeforces.com/problemset/problem/1805/B

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    smallest_char = min(s)
    smallest_char_index = s.rfind(smallest_char)
    result = s[smallest_char_index] + s[:smallest_char_index] + s[smallest_char_index + 1:]
    print(result)

