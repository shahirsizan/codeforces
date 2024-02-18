t = int(input())

for _ in range(t):
    n = int(input())
    coins_list = list(map(int, input().split()[:n]))
    sorted_coins = sorted(coins_list)

    starting_index = 0
    prefix_sum = sorted_coins[0]

    for x in range(1, len(coins_list)):
        if sorted_coins[x] > prefix_sum:
            starting_index = x
        prefix_sum += sorted_coins[x]

    winners_list = []
    win_count = 0
    for x in range(n):
        if coins_list[x] >= sorted_coins[starting_index]:
            winners_list.append(x + 1)
            win_count += 1
    print(win_count)
    print(*winners_list)

