max_length = int(input())
result = 0
for i in range(1, max_length+1):
  result = result + 2**i
print(result)

# For n = 1, there are 2^1 = 2 occurances.
# For n = 2, there are 2^1 + 2^2 = 6 occurances.
# For n = 2, there are 2^1 + 2^2 + 2^3 = 14 occurances.
# Means, for n = n, there will be 2^1 + 2^2 + 2^3 + .... + 2^n occurances