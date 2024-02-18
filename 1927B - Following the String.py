t = int(input())

for _ in range(t):
    n = int(input())
    given_trace = list(map(int, input().split()))
    last_occurrence_list = [0] * 26
    result_string = ""

    for i in range(n):
        for j in range(26):
            if given_trace[i] == last_occurrence_list[j]:
                last_occurrence_list[j] += 1
                result_string += chr(97 + j)
                break

    print(result_string)
