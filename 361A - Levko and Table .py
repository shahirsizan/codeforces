n, k = map(int, input().split())

# Initialize a 2D list with all cells being `0`
table = [[0]*n for _ in range(n)]

# Fill the diagonal celss with `k` so that each row and column sums are equal to k
for i in range(n):
    table[i][i] = k

for row in table:
    print(*row)
