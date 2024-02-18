# https://codeforces.com/problemset/problem/1740/A

small_prime_numbers_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
t = int(input())
for _ in range(t):
    given_prime = int(input())

    for x in small_prime_numbers_list:
        if (given_prime + x) % 2 == 0:
            print(x)
            break

# THERE IS ANOTHER SOLUTION. BUT THIS ONE IS NOT INDUSTRY STANDARD.
# t = int(input())
# for i in range(t):
#     print(input())