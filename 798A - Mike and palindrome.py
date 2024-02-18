given_string = input()
given_string_reversed = given_string[::-1]
c = 0
for i in range(len(given_string_reversed)):
    if given_string_reversed[i] != given_string[i]:
        c += 1
if c == 2 or (c == 0 and len(given_string)%2 != 0):
    # If `given_string_reversed` is different in two different indices than `given_string`,
    #       that means we can simply change the `given_string` at one index, and it will become plaindrome.
    # Or if `given_string_reversed` and `given_string` are equal and also of odd length, then it is
    #       already palindrome. Moreover, we can simply change the middle character which will also
    #       yield a palindrome string
    print("YES")
else:
    print("NO")
