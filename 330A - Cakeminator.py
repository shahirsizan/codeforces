r, c = map(int, input().split())

cake = [input() for _ in range(r)]

rows_with_strawberries = set()
cols_with_strawberries = set()

# Identify rows and columns with evil strawberies
for i in range(r):
    for j in range(c):
        if cake[i][j] == 'S':
            rows_with_strawberries.add(i)
            cols_with_strawberries.add(j)


cells_without_evil_strawberries = (r * c) - len(rows_with_strawberries) * len(cols_with_strawberries)

print(cells_without_evil_strawberries)
