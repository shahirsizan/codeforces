def solve(s):
    x, y = 0, 0

    for move in s:
        if move == "L":
            x -= 1
        elif move == "R":
            x += 1
        elif move == "U":
            y += 1
        elif move == "D":
            y -= 1

        if x == 1 and y == 1: # WE CHECK WHETHER THE (X,Y) COORDINATE ALONG THE JOURNEY EQUALS TO (1,1)
            return "YES"

    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()[:n]
    result = solve(s)
    print(result)
