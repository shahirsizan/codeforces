t = int(input())
for _ in range(t):
    sum_of_digits = int(input())
    result = ""
    base_pattern = '21'

    quotient, remainder = divmod(sum_of_digits, 3)
    # Returns a tuple containing the quotient and the remainder

    # Repeat the base pattern 'quotient' times
    result += base_pattern * quotient

    # Determine the remaining digits based on the `remainder`
    if remainder == 2:
        result += '2'
    elif remainder == 1:
        result = '1' + result

    print(result)

# Repeat the pattern '21' a certain number of times based on the quotient of `divmod(sum_of_digits, 3)`
# the remaining digits are determined based on the remainder of the `divmod(sum_of_digits, 3)`