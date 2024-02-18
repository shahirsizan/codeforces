t = int(input())
for _ in range(t):
    n = int(input())

    max_quality = 0
    winner_index = 0

    for i in range(1, n + 1):
        number_of_words, quality_of_the_response = map(int, input().split())

        if number_of_words <= 10 and quality_of_the_response > max_quality:
            max_quality = quality_of_the_response
            winner_index = i

    print(winner_index)
