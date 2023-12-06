t = int(input())
for _ in range(t):
    no_of_col = int(input())
    row_1 = input()
    row_2 = input()

    for i in range(no_of_col):
        # Check if two cells in the same column but in two different rows are traps('1')
        # if so, we can't go any further neither in `adjacent manner` or in `diagonal manner`.
        if row_1[i] == row_2[i] == "1":
            print("NO")
            break
    else:
        print("YES")
