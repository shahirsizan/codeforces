def minimum_gold_to_spend(n, m, characters_demand_list, friendships_tuple_list):
    pa = [ i for i in range(n+1) ]
    characters_demand_listt = [0] + characters_demand_list

    def find(i):
        while i != pa[i]:
            pa[i] = pa[pa[i]]
            i = pa[i]
        return i

    for (x,y) in friendships_tuple_list:
        x, y = find(x), find(y)
        if characters_demand_listt[x] < characters_demand_listt[y]:
            #x, y = y, x
            pa[y] = x
        else:
            pa[x] = y

    return sum( characters_demand_listt[i] for i in range(n+1) if pa[i] == i )


n, m = map(int, input().split())
characters_demand = list(map(int, input().split()))
friendships_list = [tuple(map(int, input().split())) for _ in range(m)]

result = minimum_gold_to_spend(n, m, characters_demand, friendships_list)
print(result)
