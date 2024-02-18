from collections import Counter

def solve():
    n = int(input())
    a = list( map(int, input().split()[:n]) )
    unique_elements = set()
    elements_counter = Counter(a)

    for element, number_of_occurance in elements_counter.items():
        if element in unique_elements:
            continue
        unique_elements.add(element)
        if number_of_occurance > 1:
            unique_elements.add(-element)

    print(len(unique_elements))


t = int(input())
for _ in range(t):
    solve()
