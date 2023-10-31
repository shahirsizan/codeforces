k = int(input())
count = 1
current_number = 19

while count < k:
    current_number += 9
    if sum( list( int(x) for x in str(current_number) ) ) == 10:
        count += 1

print(current_number)
