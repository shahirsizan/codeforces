t = int(input())
for _ in range(t):
    array_len, no_of_queries = map(int, input().split())
    a = list( int(i) for i in input().split() )
    sum_of_array_elements = sum(a)
    even_count = 0
    odd_count = 0

    for i in range(array_len):
        if a[i] % 2:
            odd_count += 1
        else:
            even_count += 1

    for query in range(no_of_queries):
        query_type, query_value = map(int, input().split())

        if query_type == 0:                 # add `query_value` to all the even elements
            if query_value % 2 == 0:        # if query value is even, then increment total sum with `even_count * even_query_value`
                sum_of_array_elements += even_count * query_value
            else:                           # if query value is odd, then increment total sum with `even_count * odd_query_value`
                sum_of_array_elements += even_count * query_value
                odd_count += even_count     # as even+odd=odd; all the even elements will become `odd` and
                even_count = 0              # `even_count` will become `0`

        else:                               # add `query_value` to all the odd elements
            if query_value % 2 == 0:
                sum_of_array_elements += odd_count * query_value
            else:
                sum_of_array_elements += odd_count * query_value
                even_count += odd_count     # as odd+odd=even; all the odd elements will become `even` and
                odd_count = 0               # `odd_count` will become `0`


        print(sum_of_array_elements)
