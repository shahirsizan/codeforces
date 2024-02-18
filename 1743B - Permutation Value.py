t = int(input())
for _ in range(t):
    n = int(input())
    permutation_sequence = [1] + [i for i in range(3, n+1)] + [2]
    for element in permutation_sequence:
        print(element, end=" ")
    print()
