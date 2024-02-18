t = int(input())
for _ in range(t):
    n, m = map( int, input().split() )
    print( (n//2 + 1), (m//2 + 1) )

# `n//2 + 1` calculates the row number of the isolated cell.
# Since the knight can move two cells in one direction,
# dividing the number of rows by 2 gives the middle row.
# Adding 1 ensures that the knight moves to an isolated cell.
# Same goes for column

# As for `no isolated cell available` sitution, we are allowed to print any cell
# So basically we are left with the opportunity to just print
# the middle (row,col) no matter whether there is any isolated cell or not.