no_of_days, total_study_hour = map( int, input().split() )
timetable_set_by_parents = list(list(map(int, input().split())) for _ in range(no_of_days))
total_min_hours = sum(day[0] for day in timetable_set_by_parents)
total_max_hours = sum(day[1] for day in timetable_set_by_parents)

if total_max_hours<total_study_hour or total_min_hours>total_study_hour:
    print("NO")

else:
    timetable_set_by_peter = list(day[0] for day in timetable_set_by_parents)  # starting with minimumx hours, we'll update them gradually
    remaining_total_study_hour = total_study_hour
    remaining_total_study_hour -= total_min_hours

    for i in range(no_of_days):
        if remaining_total_study_hour == 0:
            break
        else:   # gradually updating actual hours depending on remaining time
            if timetable_set_by_parents[i][1] - timetable_set_by_parents[i][0] <= remaining_total_study_hour:
                # now we'll increase `hour count` which peter will show to his parents
                timetable_set_by_peter[i] += (timetable_set_by_parents[i][1] - timetable_set_by_parents[i][0])
                remaining_total_study_hour -= (timetable_set_by_parents[i][1] - timetable_set_by_parents[i][0])
            else:
                timetable_set_by_peter[i] += remaining_total_study_hour
                remaining_total_study_hour -= remaining_total_study_hour

    print("YES")
    for i in range(no_of_days):
        print(timetable_set_by_peter[i], end=" ")
