string1 = input()
string2 = input()

index_from_RHS = -1
min_moves_required = len(string1) + len(string2)

for i in range( min(len(string1),len(string2)) ):
    if string1[index_from_RHS] == string2[index_from_RHS]:
        index_from_RHS -= 1
        min_moves_required -= 2
    else:
        break

print(min_moves_required)
