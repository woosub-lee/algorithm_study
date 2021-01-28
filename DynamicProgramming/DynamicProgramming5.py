# 효율적인 화폐구성
INF =  987654321
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
DP = [INF for _ in range(m+1)]
DP[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if DP[j - array[i]] != INF:
            DP[j] = min(DP[j], DP[j - array[i]]+1)
if DP[m] == INF:
    print(-1)
else:
    print(DP[m])
