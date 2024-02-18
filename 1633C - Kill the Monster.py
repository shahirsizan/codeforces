# https://codeforces.com/problemset/problem/1633/C
# solution: https://codeforces.com/problemset/submission/1633/223953987
import math

ans_list = list()
t = int(input())
for i in range(t):
    character_health, character_attack = map(int, input().split())
    monster_health, monster_attack = map(int, input().split())
    no_of_coins, attack_upgrade_amount, health_upgrade_amount = map(int, input().split())
    count_attack_upgrade, count_health_upgrade = 0, no_of_coins
    # we can initiate them the other way, but doesn't matter. We'll make them increase/decrease eventually


    # If the character can defeat the monster without any upgrade,
    # append "YES" and continue to next test case.
    if math.ceil(monster_health / character_attack) <= math.ceil(character_health / monster_attack):
        ans_list.append("YES")
        continue    # skip the following `while` loop go to next test case


    while count_health_upgrade >= 0:
        character_health_this_time = character_health + (count_health_upgrade * health_upgrade_amount)
        character_attack_this_time = character_attack + (count_attack_upgrade * attack_upgrade_amount)
        steps_needed_for_character_win = math.ceil(monster_health / character_attack_this_time)
        steps_needed_for_monster_win = math.ceil(character_health_this_time / monster_attack)

        if steps_needed_for_character_win <= steps_needed_for_monster_win:
            ans_list.append("YES")
            break

        count_health_upgrade -= 1
        count_attack_upgrade += 1

    else:   # This else will execute only when the above while loop exits naturally.
            # No upgrade leads to victory, append "NO".
        ans_list.append("NO")

for i in ans_list:
    print(i)
