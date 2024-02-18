# https://codeforces.com/problemset/problem/1790/D

from collections import Counter

# c = Counter('chittagonguniversityofengineering&technology')
# print("1: ",c)
# print("2: ",c.elements())
# print("4: ",list(c.keys()))
# print("5: ",list(c.values()))

t = int(input())
for _ in range(t):
    n = int(input())
    given_sizes_list = list(map(int, input().split()[:n]))
    given_sizes_list.sort()
    counter_object = Counter(given_sizes_list)
    result = 0
    unique_elements_set = sorted(set(given_sizes_list))

    for each_unique_element in unique_elements_set:
        if counter_object[each_unique_element] > counter_object[each_unique_element - 1]:
            result += (counter_object[each_unique_element] - counter_object[each_unique_element - 1])
    print(result)
