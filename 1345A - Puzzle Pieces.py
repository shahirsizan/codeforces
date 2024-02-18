t = int(input())
for _ in range(t):
    rows, cols = map(int, input().split())
    if rows + cols >= rows * cols:
        print("YES")
    else:
        print("NO")

#     Number of Tabs in Adjacent Pieces:
#         For each piece, there are three tabs.
#         If we have a grid with n rows and m columns, there are (n-1) * m pairs of adjacent rows and n * (m-1) pairs of adjacent columns.
#         So, there are a total of (n-1) * m + n * (m-1) = 2n*m - (n + m) possible pairs of adjacent pieces.
#         In each pair, one tab can fit into the blank space of the other piece. So, we need at least this number of tabs for the puzzle to be solvable.
#
#     Total Number of Tabs:
#         In n * m pieces, there are 3 * n * m tabs since each piece has 3 tabs.
#
# Therefore, if 3 * n * m >= 2n*m - (n + m), the puzzle is solvable.
# By simplifying this inequality, we get n + m <= 3. So, the puzzle is solvable
# if the number of rows and columns combined is less than or equal to 3.
# In the provided solution, it checks if rows + cols >= rows * cols, and if this condition holds,
# it means the total number of rows and columns is less than or equal to 3, and hence, the puzzle is solvable.

# SOURCE: GOOGLE
