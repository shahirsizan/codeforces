t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    array = list( map(int, input().split()) )

    # Select the elements before and after my position
    prefix = array[:m]
    suffix = array[-1 : -m-1 : -1]

    # Choose the maximum element for each step
    choices = list( max(prefix[i],suffix[m-i-1]) for i in range(m) )

    if k >= m - 1:
        result = max(choices)
    else:
        if k != 0:
            # Consider minimum values for each possible fixed choice
            min_choices = list( min(choices[i:m - k + i]) for i in range(k + 1) )
            result = max(min_choices)
        else:
            result = min(choices)

    print(result)
