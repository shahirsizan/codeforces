#https://codeforces.com/problemset/problem/1902/B
# sol: https://codeforces.com/problemset/submission/1902/236381185

from math import ceil

t = int(input())
for _ in range(t):
    no_of_days, required_point, lesson_point, task_point = map(int, input().split())
    num_of_tasks = (no_of_days - 1) // 7 + 1
    num_of_lessons = ceil(num_of_tasks / 2)


    if required_point - (num_of_tasks*task_point + num_of_lessons*lesson_point) <= 0:
        max_work_day = ceil(required_point / (2*task_point + lesson_point))
        #how many days?     #total point      #max point in a single day

    else:
        # Calculate the marks based on the remaining points after completing tasks and half the lessons
        remaining_point = required_point - (num_of_tasks*task_point + num_of_lessons*lesson_point)
        max_work_day = ceil(num_of_tasks / 2)
        max_work_day += ceil(remaining_point / lesson_point)

    print(no_of_days - max_work_day)
