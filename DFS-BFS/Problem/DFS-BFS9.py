# 연산자 끼워넣기
# 외부 소스에서 입력예제를 제공받음 (https://www.acmicpc.net/problem/18405 참조)
"""
실수했던 점:

기억해야할 점:
"""
from sys import stdin
"""
숫자개수
숫자들
연산자들

dfs를 쓸거야
dfs는 어떻게 해
depth를 기준으로 잡고 재귀를 돌아
연산자들의 리스트를 만들고
check를 해 수는 변하지 않으니까
그러고선 max와 min이면 update
"""
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