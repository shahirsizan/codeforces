# https://codeforces.com/problemset/problem/1398/B

t = int(input())
for _ in range(t):
    # get the binary string and split it at places where '0' occurs
    # if s = `101100101` => ["1", "11", "1", "1"].
    segments_list = list(input().split('0'))

    # sort `s`` in descending order and pick elements from indices 0,2,4,6... till the end
    # these are what Alice gets
    segments_list = sorted(segments_list, reverse=True)
    segments_list = segments_list[::2]

    result = sum(len(each_segment) for each_segment in segments_list)

    print(result)
