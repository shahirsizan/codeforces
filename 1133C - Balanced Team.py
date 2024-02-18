# https://codeforces.com/problemset/problem/1133/C

n = int(input())
skills_list = list(map(int, input().split()[:n]))
skills_frequency_dict = {}

for skill in skills_list:
    skills_frequency_dict[skill] = skills_frequency_dict.get(skill, 0) + 1

global_max_count = 0

for skill in skills_frequency_dict:
    max_count_so_far = 0
    for i in range(0, 6):
        max_count_so_far += skills_frequency_dict.get(skill + i, 0)
    if max_count_so_far > global_max_count:
        global_max_count = max_count_so_far

print(global_max_count)
