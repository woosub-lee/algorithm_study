# 개미전사(보텀업)
n = int(input())
array = list(map(int, input().split()))
DP = [0 for _ in range(n)]
DP[0] = array[0]
DP[1] = max(array[1], array[0])
for i in range(2, n):
    DP[i] = max(DP[i-1], DP[i-2] + array[i])
    print(DP)
print(DP[i])
