def max_books(no_of_books, free_time, time_requirement_list):
    left = 0
    right = 0
    totalTime = 0
    maxBooks = 0

    while right < no_of_books:
        totalTime += time_requirement_list[right]
        while totalTime > free_time:
            totalTime -= time_requirement_list[left]
            left += 1

        maxBooks = max(maxBooks, right - left + 1)
        right += 1

    return maxBooks

if __name__ == "__main__":
    n, t = map(int, input().split())
    time_requirement_list = list(map(int, input().split()))

    result = max_books(n, t, time_requirement_list)
    print(result)
