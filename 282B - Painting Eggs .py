n = int(input())
sum_of_A = 0
sum_of_G = 0
distribution_string = ""

for _ in range(n):
    price_A, price_G = map(int, input().split())

    if sum_of_A + price_A - sum_of_G < 500:
        sum_of_A += price_A
        distribution_string += 'A'
    else:
        sum_of_G += price_G
        distribution_string += 'G'

print(distribution_string)
