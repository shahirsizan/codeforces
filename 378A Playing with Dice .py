def count_outcomes(a, b):
    first_player_wins = 0
    second_player_wins = 0
    draws = 0

    for x in range(1, 7):
        diff_from_a = abs(a - x)
        diff_from_b = abs(b - x)

        if diff_from_a < diff_from_b:
            first_player_wins += 1
        elif diff_from_a > diff_from_b:
            second_player_wins += 1
        else:
            draws += 1

    return first_player_wins, draws, second_player_wins

if __name__ == "__main__":
    a, b = map(int, input().split())
    result = count_outcomes(a, b)
    print(*result)
