def calculate_time_to_wait(p, a, b, c):
    p_mod_a = p % a
    p_mod_b = p % b
    p_mod_c = p % c

    waiting_time_a = (a - p_mod_a) % a
    waiting_time_b = (b - p_mod_b) % b
    waiting_time_c = (c - p_mod_c) % c

    return min(waiting_time_a, waiting_time_b, waiting_time_c)


t = int(input())
for _ in range(t):
    p, a, b, c = map( int, input().split() )
    time_to_wait = calculate_time_to_wait(p, a, b, c)
    print(time_to_wait)
