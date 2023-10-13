n = int(input())
pages_per_day = list(map(int, input().split()))
day = 0

while n > pages_per_day[day]:
    n -= pages_per_day[day]
    day = (day + 1) % 7

print(day + 1)
