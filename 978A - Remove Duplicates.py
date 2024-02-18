n = int(input())
given_array = list(map(int, input().split()))

visited_list = []
result_list = []

for i in range(n-1, -1, -1):  # LOOP THROUGH THE ARRAY FROM INDEX (n-1) to 0(inclusive) backwards
    if given_array[i] not in visited_list:
        visited_list.append(given_array[i])
        result_list.append(given_array[i])

print(len(result_list))
print(" ".join(map(str, result_list[::-1])))
