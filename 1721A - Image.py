t = int(input())
for _ in range(t):
    input_str = input
    pixels = input_str() + input_str()

    # The minimum number of moves required to make all pixels the same color is calculated by
    # subtracting 1 from the count of unique colors.
    unique_colors_count = len(set(pixels))
    moves_needed = unique_colors_count - 1

    print(moves_needed)
