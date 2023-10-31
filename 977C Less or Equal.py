n, k = map(int, input().split())
a = sorted(map(int, input().split()))
if k == 0:              # GET THE ELEMENT WHICH IS `SMALLER` THAN THE `SMALLEST ELEMENT` OF THE LIST
    print(a[0] - 1 if a[0] > 1 else -1)
elif k == n:            # GET THE LAST ELEMENT OF THE LIST
    print(a[n - 1])
elif a[k - 1] == a[k]:  # a[k-1] AND a[k] ARE THE SAME, SO `EXACTLY K` CONDITION IS NOT SATISFIED
    print(-1)
else:                   # ALL'S WELL, JUST GET THE (K-1)th ELEMENT
    print(a[k - 1])
