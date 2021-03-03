# 경쟁적 전염
# 외부 소스에서 입력예제를 제공받음 (https://www.acmicpc.net/problem/18405 참조)
"""
실수했던 점: bfs를 구현하는데 어려움이 존재함

기억해야할 점: 큐로 구현하는데 성공했다.
             dfs-bfs 추가 공부 요망
             time을 큐에 같이 넣어 while queue로 돌리는데 성공
"""

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
boardSize, virusAmount = map(int, sys.stdin.readline().rstrip().split())
board = []
Virus = []
visited = [[False for i in range(boardSize)] for j in range(boardSize)]
for i in range(boardSize):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(row)
    for j in range(boardSize):
        if board[i][j] != 0:
            Virus.append([board[i][j], 0, i, j])
queue = deque(sorted(Virus))
second, yTarget, xTarget = map(int, sys.stdin.readline().rstrip().split())
while queue:
    virusKind, time, nowY, nowX = queue.popleft()
    if time == second:
        break
    if nowY+1 == yTarget and nowX+1 == xTarget:
        board[nowY][nowX] = virusKind
        break
    for i in range(4):
        if nowY+dy[i] >= 0 and nowY+dy[i] < boardSize and nowX+dx[i] >= 0 and nowX+dx[i] < boardSize:
            if board[nowY + dy[i]][nowX + dx[i]] == 0:
                board[nowY + dy[i]][nowX + dx[i]] = virusKind
                queue.append([virusKind, time+1, nowY+dy[i], nowX+dx[i]])
print(board[yTarget-1][xTarget-1])


