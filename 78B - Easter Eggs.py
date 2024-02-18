# https://codeforces.com/problemset/problem/78/B

n = int(input())
colors_list = ['V', 'I', 'B', 'G', 'Y', 'O', 'R']
egg_sequence = ""

for i in range(n - 3):
    egg_sequence = egg_sequence + colors_list[i % 4]

egg_sequence += 'YOR'

print(egg_sequence)
