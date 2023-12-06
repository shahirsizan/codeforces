n = int(input())
chat_order_dict = {}

for i in range(n):
    recipient = input()
    chat_order_dict[recipient] = i

for name in sorted( chat_order_dict.keys(), key=lambda x: chat_order_dict[x], reverse=True ):
    print(name)
