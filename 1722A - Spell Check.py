t = int(input())
for _ in range(t):
    length = input()
    string = input()
    sorted_string = sorted(string)
    if sorted_string == sorted("Timur"):
        print('YES')
    else:
        print('NO')
