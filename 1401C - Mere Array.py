def can_make_non_decreasing(original_array, sorted_array):
    min_element = min(original_array)
    orig_array_len = len(original_array)
    for i in range(orig_array_len):
        if original_array[i] != sorted_array[i] and original_array[i] % min_element != 0:
            return False

    return True


t = int(input())
for _ in range(t):
    n = int(input())
    array = list( map(int, input().split()) )
    sorted_array = sorted(array)

    if can_make_non_decreasing(array, sorted_array):
        print("YES")
    else:
        print("NO")
