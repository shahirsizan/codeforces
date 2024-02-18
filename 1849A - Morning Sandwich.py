t = int(input())
for _ in range(t):
    bread, cheese, ham = map(int, input().split())
    layer_count = 0

    # Make layer as long as bread is available
    while bread > 0:
        layer_count += 1
        bread -= 1

        # Make layer as long as cheese or ham is available
        if bread > 0:
            if cheese > 0:
                layer_count += 1
                cheese -= 1
            elif ham > 0:
                layer_count += 1
                ham -= 1
            else:
                break

    print(layer_count)
