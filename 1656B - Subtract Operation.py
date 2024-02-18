# https://codeforces.com/problemset/problem/1656/B

for _ in range(int(input())):
    n, k = map(int, input().split())
    given_list_convrtd_to_set = set(map(int, input().split()))

    result = any( (value+k in given_list_convrtd_to_set) or (value-k in given_list_convrtd_to_set) for value in given_list_convrtd_to_set)

    print("YES" if result else "NO")
