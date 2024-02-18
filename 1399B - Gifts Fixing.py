for _ in range( int(input()) ):
    n = int(input())

    candy_count = list( map(int, input().split()) )
    orange_count = list( map(int, input().split()) )

    min_candy_count = min(candy_count)
    min_orange_count = min(orange_count)
    number_of_moves = 0

    for i in range(n):
        number_of_moves += max( candy_count[i] - min_candy_count,
                                orange_count[i] - min_orange_count )

    print(number_of_moves)
