t = int(input())
for _ in range(t):
    no_of_elements, target_value = map(int, input().split())
    numbers_list = list(map(int, input().split()))

    total_sum = sum(numbers_list)

    if total_sum == target_value:
        print("YES")
    else:
        print("NO")
