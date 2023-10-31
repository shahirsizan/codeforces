# https://codeforces.com/problemset/problem/66/B

def solve(curr_index):
    watered_sections = 1

    # Simulate flow to the left
    for i in range(curr_index-1, -1, -1):
        if heights_list[i] <= heights_list[i+1]:
            watered_sections += 1
        else:
            break

    # Simulate flow to the right
    for i in range(curr_index+1, n):
        if heights_list[i] <= heights_list[i-1]:
            watered_sections += 1
        else:
            break

    return watered_sections

n = int(input())
heights_list = list( map( int, input().split()[:n] ) )
result = 0
for i in range(n):
    watered_sections_for_current_i = solve(i)
    result = max(result, watered_sections_for_current_i)

print(result)
