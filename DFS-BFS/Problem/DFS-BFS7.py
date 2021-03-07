# 연구소
# 외부에서 입력예제 제공 (https://www.acmicpc.net/problem/14502 참고)
"""
실수했던 점: dfs가 무한재귀에서 빠져나오지 못했다.

기억해야할 점:  추가 공부 요함
"""
import sys
rowSize, columnSize = map(int, sys.stdin.readline().rstrip().split())
lab = []
tempLab = [[0 for i in range(columnSize)] for j in range(rowSize)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

result = 0

for i in range(rowSize):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))


def virus(y, x):
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < rowSize and 0 <= nx < columnSize:
            if tempLab[ny][nx] == 0:
                tempLab[ny][nx] = 1
                virus(ny, nx)


def getSafeScore():
    score = 0
    for y in range(rowSize):
        for x in range(columnSize):
            if tempLab[y][x] == 0:
                score += 1
    return score


def dfs(count):
    global result
    global tempLab
    if count == 3:
        for y in range(rowSize):
            for x in range(columnSize):
                tempLab[y][x] = lab[y][x]

        for y in range(rowSize):
            for x in range(columnSize):
                if tempLab[y][x] == 2:
                    virus(y, x)
        result = max(result, getSafeScore())
        return

    for y in range(rowSize):
        for x in range(columnSize):
            if lab[y][x] == 0:
                lab[y][x] = 1
                count += 1
                dfs(count)
                lab[y][x] = 0
                count -= 1


dfs(0)
print(result)