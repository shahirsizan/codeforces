t = int(input())
for _ in range(t):
    no_of_frnds, no_of_unique_gifts = map(int, input().split())
    assigned_numbers_list = sorted([int(i) for i in input().split()])
    gifts_prices_list = [''] + [int(i) for i in input().split()]
    i, result = 1, 0
    for assigned_number in assigned_numbers_list[::-1]:
        if assigned_number >= i:
            result += gifts_prices_list[i]
            i += 1
        else:
            result += gifts_prices_list[assigned_number]
    print(result)
