n = int(input())
beauty_values_list = list( map(int, input().split()) )

adjusted_beauty_values_list = list( beauty_values_list[i]-i for i in range(n) )
beauty_dict = {}

for i in range(n):
    if adjusted_beauty_values_list[i] not in beauty_dict:
        beauty_dict[adjusted_beauty_values_list[i]] = beauty_values_list[i]
    else:
        beauty_dict[adjusted_beauty_values_list[i]] += beauty_values_list[i]

print( max(list(beauty_dict.values())) )
