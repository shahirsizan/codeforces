t = int(input())
for _ in range(t):
    n = int(input())
    hero_levels = list(map(int, input().split()[:n]))

    # WE FIRST FIND THE MIN POWERED HERO.
    # THEN WE HAVE TO FIND THE NUMBER OF HEROES WHOSE POWER IS STRICTLY GREATER THAN THE MIN POWERED ONE
    # THEY ALL ARE THE POSSIBLE WINNERS, BECAUSE THEY CAN FIGHT WITH THE WEAKEST HERO OVER AND OVER AGAIN
    # AND EVENTUALLY BECOME A WINNER

    min_power = min(hero_levels)
    possible_winners = len(hero_levels) - hero_levels.count(min_power)

    print(possible_winners)
