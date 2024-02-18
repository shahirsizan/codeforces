n = int(input())
s = input()

num_zeros = s.count("z")
num_ones = s.count("n")

print("1 " * num_ones + "0 " * num_zeros)
