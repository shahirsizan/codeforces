# https://codeforces.com/problemset/problem/445/A

rows, columns = map(int, input().split())
chessboard = []

for i in range(rows):
    given_row = list(input())
    for j in range(columns):
        if given_row[j] == '.':
            if (i + j) % 2 == 1:
                given_row[j] = 'B'
            else:
                given_row[j] = 'W'
    print("".join(given_row))
