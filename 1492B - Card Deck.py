t = int(input())
for _ in range(t):
    n = int(input())
    deck_values_list = list(map(int, input().split()))
    # values_encountered_so_far_list = list()
    # GOT ME TIME EXCEEDED ERROR.
    # Sets are implemented as hash tables, which allows for very fast membership testing.
    # Checking if an element is in the set with an average time complexity of O(1).
    # Lists have to iterate through each element in sequence,
    # resulting in an average time complexity of O(n) for membership testing.

    values_encountered_so_far_set = set()
    expected_max_value = n
    last_index_of_the_future_subarray = n
    ans_list = list()

    for i in range(n-1, -1, -1):
        if deck_values_list[i] == expected_max_value:
            ans_list += deck_values_list[i:last_index_of_the_future_subarray]
            last_index_of_the_future_subarray = i
            values_encountered_so_far_set.add(deck_values_list[i])
            while (expected_max_value in values_encountered_so_far_set) and (expected_max_value >= 0):
                expected_max_value -= 1
        else:
            values_encountered_so_far_set.add(deck_values_list[i])

    print(*ans_list)
