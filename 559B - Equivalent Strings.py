def generate_partition(s):
    length = len(s)
    return sorted([ generate_partition( s[:length//2] ), generate_partition( s[length//2:] ) ]) if length % 2 == 0 else s

string1 = input()
string2 = input()

if generate_partition(string1) == generate_partition(string2):
    print('YES')
else:
    print('NO')
