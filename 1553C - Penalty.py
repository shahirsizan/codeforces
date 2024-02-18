# https://codeforces.com/problemset/problem/1553/C

t = int(input())

for _ in range(t):
    given_string = input()
    first_team_current_goal = 0
    first_team_stop_at = 10

    for i in range(10):
        if i % 2 == 0:  # 0,2,4,6,8 for first team
            if given_string[i] == "?":
                first_team_current_goal += 1
            else:
                first_team_current_goal += int(given_string[i])
        else:           # 1,3,5,7,9 for second team
            if given_string[i] != "?":
                first_team_current_goal -= int(given_string[i])

        # 1? 0? 1? 10 01
        if first_team_current_goal > (10-i)//2:
            first_team_stop_at = i + 1      # i is current index
            break

    second_team_current_goal = 0
    second_team_stop_at = 10
    for i in range(10):
        if i % 2 == 0:      # 0,2,4,6,8 for first team
            if given_string[i] != "?":
                second_team_current_goal -= int(given_string[i])
        else:               # 1,3,5,7,9 for second team
            if given_string[i] == "?":
                second_team_current_goal += 1
            else:
                second_team_current_goal += int(given_string[i])

        # 1? 0? 1? 10 01
        if second_team_current_goal > (9-i)//2:
            second_team_stop_at = i + 1
            break

    result =  min(first_team_stop_at, second_team_stop_at)
    print(result)



