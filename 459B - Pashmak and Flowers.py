n = int(input())
flowers_beauty_list = list(map(int, input().split()))
flowers_beauty_list.sort()

max_beauty_difference = flowers_beauty_list[-1] - flowers_beauty_list[0]
min_beauty_count = flowers_beauty_list.count(flowers_beauty_list[0])
max_beauty_count = flowers_beauty_list.count(flowers_beauty_list[-1])

if max_beauty_difference == 0:
    number_of_ways_to_pick = n*(n-1)//2
else:
    number_of_ways_to_pick = min_beauty_count * max_beauty_count

print(max_beauty_difference, number_of_ways_to_pick)
