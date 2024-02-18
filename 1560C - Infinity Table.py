import math

t = int(input())
for _ in range(t):
    k = int(input())

    possible_column = math.ceil(math.sqrt(k))
    top_right_corner_value = pow(possible_column,2) - possible_column + 1

    if k >= top_right_corner_value:
        row = possible_column
        col = possible_column - (k - top_right_corner_value)
    else:
        row = k - top_right_corner_value + possible_column
        col = possible_column

    print(row, col)
