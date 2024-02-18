t = int(input())
for _ in range(t):
    n = int(input())
    elements_list = list( map(int, input().split()) )
    odd_count = 0
    even_count = 0

    for i in range(n):
        if elements_list[i]%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # as `even+even=even` and `odd+odd=even`,
    # so we try to make list consisting of either even or odd elements, no mixed type of elements.
    # only then the sum of two consecutive elements will yield `even`
    print( min(odd_count, even_count) )
