# https://codeforces.com/problemset/problem/1293/B

n = int(input())
total_reward = 0

for i in range(n, 0, -1):
    total_reward += 1/i

print(total_reward)
