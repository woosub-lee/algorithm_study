# 1로만들기
number = int(input())
DP = [0 for _ in range(number+1)]
for i in range(2, number+1):
    DP[i] = DP[i-1] + 1
    if i % 2:
        DP[i] = min(DP[i], DP[i // 2] + 1)
    if i % 3:
        DP[i] = min(DP[i], DP[i // 3] + 1)
    if i % 5:
        DP[i] = min(DP[i], DP[i // 5] + 1)
print(DP)
