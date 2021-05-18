# 숫자의 신
# 외부에서 입력을 제공받음 (https://www.acmicpc.net/problem/1422 참고)
"""
실수했던 점: 람다식으로 소트를 진행하기에 어려움을 느껴 버블정렬의 아이디어로 정렬을 구현함

기억해야할 점: maxValue를 구하는 구현식을 간단히 할 수 있을 것 같음
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write
numberCount, targetCount = map(int, input().rstrip().split())
numbers = []
result = ""
maxValue = "0"
for i in range(numberCount):
    isBigger = False
    numbers.append(input().rstrip())
    if len(numbers[i]) > len(maxValue):
        isBigger = True
    elif len(numbers[i]) == len(maxValue):
        if int(numbers[i]) > int(maxValue):
            isBigger = True
    if isBigger:
        maxValue = numbers[i]
numbers = numbers + [maxValue for i in range(targetCount-numberCount)]
for i in range(targetCount-1, 0, -1):
    for j in range(i):
        if int(numbers[j]+numbers[j+1]) < int(numbers[j+1]+numbers[j]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in range(targetCount):
    result = result + numbers[i]
print(result)
