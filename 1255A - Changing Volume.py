def min_presses_needed(a, b):
    volume_diff = abs(a - b)
    min_presses_needed = (volume_diff//5) + ((volume_diff%5)//2) + ((volume_diff%5)%2)
                           # hom many `5`        how many `2`           how many `1`
    return min_presses_needed

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = min_presses_needed(a, b)
    print(result)
