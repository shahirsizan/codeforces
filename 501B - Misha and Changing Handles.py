no_of_requests = int(input())
handle_map = {}

for _ in range(no_of_requests):
    old, new = input().split()

    if old in handle_map:
        handle_map[new] = handle_map.pop(old)
    else:
        handle_map[new] = old

print(len(handle_map))
for new, old in handle_map.items():
    print(old, new)
