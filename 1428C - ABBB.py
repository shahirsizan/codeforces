# https://codeforces.com/problemset/problem/1428/C

t = int(input())
for _ in range(t):
    given_string = input()
    stack = list()
    for char in given_string:
        if len(stack) != 0 and ( (stack[-1] == 'A' and char == 'B') or (stack[-1] == 'B' and char == 'B') ):
            stack.pop()
            continue
        else:
            stack.append(char)
    print(len(stack))
