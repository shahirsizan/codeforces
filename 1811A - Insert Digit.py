t = int(input())

def result(n, d, number):
    # Convert `number` to a list called `digits_list`
    digits_list = list(map(int, number))

    # Iterate through `digits_list` to find the position to insert the additional digit `d`
    for i in range(len(digits_list)):
        # If the current digit `digits_list[i]` is less than the additional digit `d`,
        # then make digits_list[i] <= d
        if d > digits_list[i]:
            digits_list.insert(i, d)
            break
    else:
        # The additional digit `d` is `smaller than or equal to` the smallest element of `digits_list`
        # so append it to the last posiiton
        digits_list.append(d)

    return ''.join(map(str, digits_list))

for _ in range(t):
    n, d = map(int, input().split())
    number = input().strip()
    print(result(n, d, number))
