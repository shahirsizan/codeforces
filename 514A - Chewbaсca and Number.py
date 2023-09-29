skywalker_gave = str(int(input()))
result = ""

for indexx, individual_digit in enumerate(skywalker_gave):
    individual_digit = int(individual_digit)
    if indexx == 0 and individual_digit == 9:
        result += str(individual_digit)
    else:
        result += str( min(individual_digit, 9-individual_digit) )

print(int(result))
