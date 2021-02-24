# 뱀
# 입력이 외부에서 주어짐 (https://www.acmicpc.net/problem/3190 참조)
"""
실수했던점: 보드에 일일이 뱀의 크기, 위치 정보를 포함할 필요가 없었다.

기억해야할 점: 입력의 크기가 작아서 완전탐색으로 진행해도 충분히 해결할 수 있었음
             큐를 이용하여 뱀의 좌표이동을 쉽게 구현해 낼수 있었다.
             확장 보드를 만들어 조건을 처리하기에 쉬웠음
"""
import sys
from collections import deque

snake = deque([[1, 1]])
boardSize = int(sys.stdin.readline().rstrip())
# 보드 외곽선 확장 및 금지구역으로 설정
board = [[0 for i in range(boardSize + 2)] for j in range(boardSize + 2)]
for y in range(len(board)):
    for x in range(len(board)):
        if y == 0 or y == len(board) - 1 or x == 0 or x == len(board) - 1:
            board[y][x] = 1

# 사과 위치 설정
appleAmount = int(sys.stdin.readline().rstrip())
for i in range(appleAmount):
    appleY, appleX = map(int, sys.stdin.readline().rstrip().split())
    board[appleY][appleX] = 2

# 커맨드 입력
commandAmount = int(sys.stdin.readline().rstrip())
Commands = deque()
for i in range(commandAmount):
    command = list(sys.stdin.readline().rstrip().split())
    Commands.append(command)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0
endTime = 0
nowCommand = Commands.popleft()
for i in range(1, int(Commands[-1][0])+boardSize):
    snake.append([snake[-1][0] + dy[direction], snake[-1][1] + dx[direction]])
    head = snake.pop()
    if board[head[0]][head[1]] == 1 or head in snake:
        endTime = i
        break
    snake.append(head)
    if board[snake[-1][0]][snake[-1][1]] != 2:
        snake.popleft()
    else:
        board[snake[-1][0]][snake[-1][1]] = 0
    if i == int(nowCommand[0]):
        if nowCommand[1] == 'D':
            direction += 1
        else:
            direction -= 1
        direction %= 4
        if Commands:
            nowCommand = Commands.popleft()
print(endTime)