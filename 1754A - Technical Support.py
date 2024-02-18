t = int(input())
for _ in range(t):
    n = int(input())
    message_sequence = input()
    stack = []

    for message_type in message_sequence:
        if message_type == "Q":
            # Client question, push to stack
            stack.append(message_type)
        else:
            # Support managers answer. If there is any pending client question in stack, pop one from it.
            if stack:
                stack.pop()

    if not stack:
        print("Yes")
    else:
        print("No")
