n, k = map(int, input().split())

participation_count_list = list(map(int, input().split()[:n]))

eligible_students = sum(list(1 for p in participation_count_list if 5-p >= k))

max_teams = eligible_students // 3

print(max_teams)
