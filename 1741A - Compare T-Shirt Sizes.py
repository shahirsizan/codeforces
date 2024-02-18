t = int(input())
for _ in range(t):
    size_a, size_b = input().split(" ")
    size_order_dict = {'S': 1, 'M': 2, 'L': 3}

    if size_order_dict[ size_a[-1] ] < size_order_dict[ size_b[-1] ]:
        result = '<'

    elif size_order_dict[ size_a[-1] ] > size_order_dict[ size_b[-1] ]:
        result = '>'

    elif len(size_a) == len(size_b):
        result = '='


    elif size_a[-1] == 'S':
        result = '<' if len(size_a) > len(size_b) else '>'

    else:
        result = '>' if len(size_a) > len(size_b) else '<'

    print(result)
