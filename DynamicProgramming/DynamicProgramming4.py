# 바닥공사 타일링(보텀업)
number = int(input())
DP = [0 for _ in range(number+1)]
DP[1] = 1
DP[2] = 3
for i in range(3, number+1):
    DP[i] = (DP[i-1] + 2*DP[i-2]) % 796796
print(DP[i])
