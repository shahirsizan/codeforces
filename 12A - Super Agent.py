first_row = input()
second_row = input()
third_row = input()

if (first_row[::-1] == third_row) and (second_row[::-1] == second_row):
    print("YES")
else:
    print("NO")
