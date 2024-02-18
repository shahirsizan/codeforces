t = int(input())
for _ in range(t):
    input_string = input().strip()

    palindrome_string = input_string + input_string[::-1]

    print(palindrome_string)
