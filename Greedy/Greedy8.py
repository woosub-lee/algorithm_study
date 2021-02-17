# 만들 수 없는 금액
# N개의 동전이 있을 때 만들 수 없는 금액중 최솟값
NumberOfCoin = int(input())
Coins = list(map(int, input().split()))
Coins = sorted(Coins)
Target = 1
for coin in Coins:
    if coin > Target:
        break
    Target += coin
print(Target)

