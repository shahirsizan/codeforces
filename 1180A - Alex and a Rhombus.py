# https://codeforces.com/problemset/problem/1180/A

def count_squares(n):
    return n**2 + (n-1)**2

n = int(input())
result = count_squares(n)
print(result)

# the formula used to calculate the number of squares in the particular rhombus is
# n^2 + (n−1)^2.