# THIS CODE IS TO DERIVE THE CYPHERTEXT FROM THE PLAIN TEXT
# n = int(input())
# s = input()
#
# for i in range(n-1, -1, -1):
#     if n % (i+1) == 0:
#         selected_part = s[ : i+1]
#         inverted_part = selected_part[ : : -1]
#         s = inverted_part + s[i+1 : ]
#
# print(s)


# THIS CODE IS TO DERIVE THE PLAIN TEXT FROM THE CYPHERTEXT
n = int(input())
s = input()

for i in range(n):
    if n % (i+1) == 0:
        selected_part = s[ : i+1]
        inverted_part = selected_part[ : : -1]
        s = inverted_part + s[i+1 : ]

print(s)