# 연산자 끼워넣기
# 외부 소스에서 입력예제를 제공받음 (https://www.acmicpc.net/problem/14888 참조)
"""
실수했던 점: check함수의 numbers의 인덱싱이 잘못 됬었다.

기억해야할 점: 재귀함수로 dfs를 구현할 수 있었다.
"""
from sys import stdin
minResult = 987654321
maxResult = -987654321
numberCount = int(input())
operatorCount = numberCount-1
operatorKind = ['+', '-', '*', '/']
numbers = list(map(int, stdin.readline().rstrip().split()))
operators = list(map(int, stdin.readline().rstrip().split()))
def check(operators):
    value = numbers[0]
    for i in range(1, len(operators)+1):
        if operators[i-1] == '+':
            value += numbers[i]
        elif operators[i-1] == '-':
            value -= numbers[i]
        elif operators[i-1] == '*':
            value *= numbers[i]
        elif operators[i-1] == '/':
            if value >= 0:
                value = value//numbers[i]
            else:
                value = abs(value)
                value = value//numbers[i]
                value *= -1

    return value

def dfs(depth, operatorList):
    global operators
    global maxResult
    global minResult
    if depth == operatorCount:
        temp = check(operatorList)
        maxResult = max(maxResult, temp)
        minResult = min(minResult, temp)
        return
    for i in range(4):
        if operators[i] != 0:
            operatorList.append(operatorKind[i])
            operators[i] -= 1
            dfs(depth+1, operatorList)
            operatorList.pop(len(operatorList)-1)
            operators[i] += 1




dfs(0, [])
print(maxResult)
print(minResult)
