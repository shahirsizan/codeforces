def form_team(n, team_size, ratings_list):
    rating_set = set(ratings_list)

    if len(rating_set) >= team_size:
        print("YES")
        team = []
        for i, rating in enumerate(ratings_list):
            if rating in rating_set:
                team.append(i + 1)
                rating_set.remove(rating)
                team_size -= 1
                if team_size == 0:
                    break
        print(*team)
    else:
        print("NO")

if __name__ == "__main__":
    n, k = map(int, input().split())
    ratings = list(map(int, input().split()))
    form_team(n, k, ratings)
