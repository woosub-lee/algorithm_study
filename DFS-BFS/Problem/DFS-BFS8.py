# 경쟁적 전염
# 외부 소스에서 입력예제를 제공받음 (https://www.acmicpc.net/problem/18405 참조)
"""
실수했던 점: bfs를 구현하는데 어려움이 존재함

기억해야할 점: 시간 복잡도를 줄이기 위해 노력해야함
"""

import sys
from collections import deque


def isInBoard(boardSize, nowPosition):
    if nowPosition[0] < 0 or nowPosition[0] >= boardSize:
        return False
    if nowPosition[1] < 0 or nowPosition[1] >= boardSize:
        return False
    return True

def bfs(array, now):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    virus = array[now[0]][now[1]]
    for i in range(4):
        position = [now[0]+dx[i], now[1]+dy[i]]
        if isInBoard(len(array), position):
            if array[position[0]][position[1]] == 0:
                array[position[0]][position[1]] = virus

boardSize, virusAmount = map(int, sys.stdin.readline().rstrip().split())
board = []
for i in range(boardSize):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(row)
second, yTarget, xTarget = map(int, sys.stdin.readline().rstrip().split())
for i in range(second):
    extendVirus = []
    for y in range(boardSize):
        for x in range(boardSize):
            if board[y][x] != 0:
                if not board[y][x] in extendVirus:
                    extendVirus.append(board[y][x])
                    bfs(board, [y, x])

print(board[yTarget-1][xTarget-1])
