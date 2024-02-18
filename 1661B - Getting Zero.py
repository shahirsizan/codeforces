import sys

n = int(input())
integers_list = list(map(int, input().split()[:n]))

for integer in integers_list:
    operations = sys.maxsize

    for j in range(integer, integer+15):
        operations_required = j - integer
        k = 0

        while j % 32768 != 0 and operations_required < 15:
            j = (2 * j) % 32768
            operations_required += 1

        operations = min(operations, operations_required)

    print(operations, end=" ")
