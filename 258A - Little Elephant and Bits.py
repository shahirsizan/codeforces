# https://codeforces.com/problemset/problem/258/A

binary_number = input()

# we want to delete the left-most-occurance of `0` (MSB)
# so that once deleted, the remaining bits together make the largest decimal number
index_of_left_most_zero = binary_number.find('0')
if index_of_left_most_zero != -1:
    binary_number = binary_number[:index_of_left_most_zero] + binary_number[index_of_left_most_zero + 1:]

# if failed to do so, we simply delete the right-most-digit (LSB)
# so that the resultant decimal digit remains as large as possible
else:
    binary_number = binary_number[:-1]

print(binary_number)
