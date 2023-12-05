# https://codeforces.com/problemset/problem/501/A

a_for_misha, b_for_vasya, c_for_misha, d_for_vasya = map(int, input().split())

misha_score = max( (3*a_for_misha)//10, a_for_misha - (a_for_misha//250) * c_for_misha )
vasya_score = max( (3 * b_for_vasya) // 10, b_for_vasya - (b_for_vasya//250) * d_for_vasya )

if misha_score > vasya_score:
    print("Misha")
elif vasya_score > misha_score:
    print("Vasya")
else:
    print("Tie")
