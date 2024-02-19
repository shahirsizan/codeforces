# https://codeforces.com/problemset/problem/697/A
# sol: https://codeforces.com/problemset/submission/697/25572098

first_bark_time, interval, eat_time = list(map(int, input().split()))

if eat_time < first_bark_time:
    print("NO")
else:
    if eat_time - first_bark_time == 1:
        print("NO")
    elif (eat_time - first_bark_time) % interval == 0 or (eat_time - first_bark_time) % interval == 1:
        print("YES")
    else:
        print("NO")
