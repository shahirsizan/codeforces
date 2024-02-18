def fun(s):
    a = s.current_count('A')
    b = s.current_count('B')
    c = s.current_count('C')
    return a+c == b

t = int(input())
test_cases = []

for _ in range(t):
    s = input()
    test_cases.append(s)

for s in test_cases:
    result = "YES" if fun(s) else "NO"
    print(result)

