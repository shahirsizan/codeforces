n = int(input())
array = list(map(int, input().split()[:n]))
sorted_a = sorted(array)

if array == sorted_a:
    print("yes")
    print("1 1")

else:
    left_index, right_index = 0, n-1

    while left_index < n-1 and array[left_index] < array[left_index+1]:
        left_index += 1

    while right_index > 0 and array[right_index] > array[right_index-1]:
        right_index -= 1

    segment = array[ : left_index] + list( reversed( array[left_index : right_index+1] ) ) + array[right_index+1 : ]

    if segment == sorted_a:
        print("yes")
        print(left_index + 1, right_index + 1)
    else:
        print("no")
