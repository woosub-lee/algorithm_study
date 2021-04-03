# 안테나
# 외부에서 입력예제 제공 (https://www.acmicpc.net/problem/18310 참고)
"""
실수했던 점: 값이 아닌 인덱스를 출력함

기억해야할 점: sort한 후 중간값이 항상 합이 가장 작은 값이었다.
"""
from sys import stdin
houseCount = int(input())
houses = list(map(int, stdin.readline().rstrip().split()))
houses = sorted(houses)
if houseCount % 2 == 1:
    print(houses[int(houseCount/2)])
else:
    temp1 = [abs(house-houses[int(houseCount/2)]) for house in houses]
    temp2 = [abs(house-houses[int(houseCount/2)-1]) for house in houses]
    if sum(temp1) >= sum(temp2):
        print(houses[int(houseCount/2)-1])
    else:
        print(houses[int(houseCount/2)])
    