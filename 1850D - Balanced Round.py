t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    difficulty_levels_sorted = sorted( list(map(int, input().split())) )
    current_max_count = 1
    global_max_count = 1

    for i in range(n-1):
        if (difficulty_levels_sorted[i+1] - difficulty_levels_sorted[i]) <= k:
            current_max_count += 1
            if current_max_count > global_max_count:
                global_max_count = current_max_count
        else:
            current_max_count = 1

    print(n - global_max_count)
