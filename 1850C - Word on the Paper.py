def extract_word_from_column(column_char_list):
    word = ""
    for char in column_char_list:
        if char != '.':
            word += char
    return word


t = int(input())
for _ in range(t):
    grid_board = [ input() for _ in range(8) ]
    word = ""

    for col in range(8):
        column_char_list = [ grid_board[row][col] for row in range(8) ]
        current_column_word = extract_word_from_column(column_char_list)
        word += current_column_word

        if word != "":
            break

    print(word)
