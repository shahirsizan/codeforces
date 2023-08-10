n = int(input())
cards_list = list(map(int, input().split()[:n]))

score_sareja = 0
score_dima = 0
left = 0
right = n - 1
turn_for_sareja = True

while left <= right:
    if turn_for_sareja:
        score_sareja += max(cards_list[left], cards_list[right])
        if cards_list[left] > cards_list[right]:
            left += 1
        else:
            right -= 1

    elif not turn_for_sareja:
        score_dima += max(cards_list[left], cards_list[right])
        if cards_list[left] > cards_list[right]:
            left += 1
        else:
            right -= 1

    turn_for_sareja = not turn_for_sareja

print(score_sareja, score_dima)
