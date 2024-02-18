t = int(input())
for _ in range(t):
    string_length = int(input())
    given_string = input()
    min_erase_required = float('inf')
    char_set = set(given_string)

    for particular_char in char_set:
        erase_required = 0
        left_index = 0
        right_index = string_length-1

        while left_index <= right_index:
            if given_string[left_index] != given_string[right_index]:
                if given_string[left_index] == particular_char:
                    left_index += 1
                    erase_required += 1
                elif given_string[right_index] == particular_char:
                    right_index -= 1
                    erase_required += 1
                else:
                    erase_required = float('inf')      # this word cannot be made palindrome for
                                                       # this `particular_char`
                    break
            else:
                left_index += 1
                right_index -= 1

        min_erase_required = min(min_erase_required, erase_required)

    if min_erase_required == float('inf'):
        print(-1)
    else:
        print(min_erase_required)