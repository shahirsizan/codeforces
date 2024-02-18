# https://codeforces.com/problemset/problem/1692/E

t = int(input())
results_list = list()

for _ in range(t):
    max_subarray_length_till_now = 0
    n, required_sum = map(int, input().split())
    given_array = list(map(int, input().split()[:n]))
    total_sum = sum(given_array)

    if total_sum == required_sum:
        results_list.append(0)
    elif total_sum < required_sum:
        results_list.append(-1)






    else:       # ekhan theke ashol kaj shuru
        _count = 0
        current_sum = 0
        left_index = 0
        right_index = 0
        for i in range(n):  # initial subarray that yields sum equal to `required_sum`
            current_sum += given_array[i]
            _count += 1
            if current_sum == required_sum:
                right_index = i + 1
                break
        max_subarray_length_till_now = _count   # first subarray er length


        i = right_index
        #for i in range(right_index, n):
        while i < n:
            j = i
            while j < n:
                if given_array[j] == 1:
                    break
                _count += 1
                max_subarray_length_till_now = max(max_subarray_length_till_now, _count)
                j += 1

            i = j
            if i == n:
                break

            while left_index < n:
                if given_array[left_index] == 1:
                    left_index += 1
                    i += 1
                    break
                _count -= 1
                left_index += 1
                max_subarray_length_till_now = max(max_subarray_length_till_now, _count)



        results_list.append(n - max_subarray_length_till_now)

print(*results_list)
