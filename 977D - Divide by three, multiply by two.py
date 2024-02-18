# https://codeforces.com/problemset/problem/977/D

def rearrange_sequence(n, given_sequence):
    result = list()
    flag = 0
    for _ in range(n):

        if flag == 1:
            break

        for num in given_sequence:
            if num * 2 in given_sequence or (num % 3 == 0 and num // 3 in given_sequence):
                continue
            else:
                result.append(num)
                given_sequence.remove(num)
            if len(given_sequence) == 0:
                flag = 1

    return result[::-1]


n = int(input())
given_sequence = list(map(int, input().split()[:n]))
rearranged_sequence = rearrange_sequence(n, given_sequence)
print(*rearranged_sequence)
