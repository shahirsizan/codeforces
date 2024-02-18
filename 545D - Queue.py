n = int(input())
serving_times_list = list(map(int, input().split()[:n]))
serving_times_list.sort()
not_disappointed_customer = 0
total_waiting_time_so_far = 0

for current_serving_time in serving_times_list:
    if current_serving_time >= total_waiting_time_so_far:
        total_waiting_time_so_far += current_serving_time
        not_disappointed_customer += 1

print(not_disappointed_customer)
