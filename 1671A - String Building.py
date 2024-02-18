import re

t = int(input())
for _ in range(t):
    input_string = input().strip()
    if re.fullmatch(r"((aa)|(aaa)|(bb)|(bbb))*", input_string):
        print("YES")
    else:
        print("NO")

# `*` matches zero or more occurrences of the
# preceding pattern. Putting it all together:
# ((bb)|(bbb)|(aa)|(aaa))*
# matches any string consisting of zero or more occurrences
# of "bb," "bbb," "aa," or "aaa."