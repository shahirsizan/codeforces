# https://codeforces.com/problemset/problem/387/B?locale=en

n, m = map(int,input().split())
complexity_requirement_list = list(map(int, input().split()))
georges_problems_list = list(map(int, input().split()))

additional_problems_needed = 0

for required_complexity in complexity_requirement_list:
    problem_permissible = False

    for given_complexity in georges_problems_list:
        if given_complexity >= required_complexity:
            problem_permissible = True
            georges_problems_list.remove(given_complexity)
            # this line is required as a contest cannot have more than one problem with the
            # same difficulty level. So as soon as we encounter a permissible_problem from
            # georges list, we can remove it. This will improve time complexity.
            break

    if not problem_permissible:
        additional_problems_needed += 1

print(additional_problems_needed)
