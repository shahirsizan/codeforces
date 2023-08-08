n , a = map(int, input().split())
a -= 1
b = [1]*n + list(map(int,input().split()[:n])) + [1]*n
print( sum(b[n+a-abs(a-x)] * b[n+a+abs(a-x)] for x in range(n)) )