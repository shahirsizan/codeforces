# # THE CODE BELOW YIELDS TIME EXCEEDE ERROR
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()[:n]))
#
#     while len(set(a)) != len(a):
#         a.pop(0)
#
#     print(n - len(a))
#
# '''
# We iteratively remove elements from the beginning of the list and check
# if the modified list length equal to the set derived from it.
# Once all elements of the list become distinct, the length of it and the length
# of the set derived from it will become equal.
# '''
# #############################################################################################################

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()[:n]
    distinct_elements = set()

    # Iterate through the sequence in reverse order
    i = n - 1
    while i >= 0:
        if a[i] not in distinct_elements:
            distinct_elements.add(a[i])
        else:
            break
        i -= 1

    print(i + 1)
