# https://codeforces.com/contest/1927/problem/A
t = int(input())
for _ in range(t):
    n = int(input())
    given_string = input().strip()

    first_occurance_of_B = given_string.find('B')
    last_occurance_of_B = given_string.rfind('B')

    min_length = last_occurance_of_B - first_occurance_of_B + 1

    print(min_length)
