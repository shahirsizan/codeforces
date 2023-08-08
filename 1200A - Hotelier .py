n = int(input())
events_list = input()[:n]
rooms = ['0'] * 10

for event in events_list:
    if event == 'L':
        empty_index = rooms.index('0')
        rooms[empty_index] = '1'
    elif event == 'R':
        empty_index = abs((rooms[::-1].index('0'))-9)
        rooms[empty_index] = '1'
    else:
        rooms[int(event)] = '0'


print(''.join(rooms))
