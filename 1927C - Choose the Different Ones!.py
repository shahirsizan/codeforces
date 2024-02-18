# https://codeforces.com/contest/1927/problem/C

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    list_a_occurances_dict = dict()
    list_b_occurances_dict = dict()
    result_list = list()

    for i in list_a:
        if (i <= k) and (i not in list_a_occurances_dict):
            list_a_occurances_dict[i] = 1
            result_list.append(i)

    for i in list_b:
        if (i <= k) and (i not in list_b_occurances_dict):
            list_b_occurances_dict[i] = 1
            result_list.append(i)

    result_set = set(result_list)

    if len(list_a_occurances_dict) >= k // 2 \
            and len(list_b_occurances_dict) >= k // 2 \
            and len(result_set) == k:
        print("YES")
    else:
        print("NO")
