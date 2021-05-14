# 동전 0
# 외부코드에서 입력을 제공받음 (https://www.acmicpc.net/problem/11047 참고)
"""
실수했던 점: 그리디를 성공적으로 구현함

기억해야할 점: 모든 동전이 배수관계에 있어 그리디 알고리즘을 사용할 수 있었음
"""
import sys
input = sys.stdin.readline
coins = []
answer = 0
coinCount, targetMoney = map(int, input().rstrip().split())
for i in range(coinCount):
    coins.append(int(input()))
coins = coins[::-1]
index = 0
while targetMoney != 0:
    if coins[index] <= targetMoney:
        answer += targetMoney//coins[index]
        targetMoney = targetMoney%coins[index]
    index += 1
print(answer)