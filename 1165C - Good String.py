n = int(input())
given_string = input()[:n]

answer = ""
i = 0
while i < n:
    if ( i < n-1 ) and ( given_string[i] != given_string[i+1] ):
        answer = answer + given_string[i] + given_string[i+1]
        i += 2
    else:
        i += 1

no_of_char_to_delete = n - len(answer)

print(no_of_char_to_delete)
print(answer)
