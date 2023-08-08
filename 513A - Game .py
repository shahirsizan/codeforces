n1, n2, k1, k2 = map(int, input().split())

if n1 > n2:
    print("First")
else:
    print("Second")

'''
Each player can take from 1 to k1 balls (for the first player) or 
from 1 to k2 balls (for the second player) in each move.
So each player would try to throw as less balls as possible, possibly 1.
So, the one with more balls in their box will eventually win.
'''