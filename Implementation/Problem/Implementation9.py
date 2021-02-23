import sys
from collections import deque

def print2D(array):
    for row in array:
        print(row)
    print()



snakeBody = deque()
snakeHead = [1, 1]
boardSize = int(sys.stdin.readline().rstrip())
board = [[0 for i in range(boardSize + 2)] for j in range(boardSize + 2)]
for y in range(len(board)):
    for x in range(len(board)):
        if y == 0 or y == len(board) - 1 or x == 0 or x == len(board) - 1:
            board[y][x] = 1
board[1][1] = 3

appleAmount = int(sys.stdin.readline().rstrip())
for i in range(appleAmount):
    appleY, appleX = map(int, sys.stdin.readline().rstrip().split())
    board[appleY][appleX] = 2

commandAmount = int(sys.stdin.readline().rstrip())
Commands = deque()
for i in range(commandAmount):
    command = list(sys.stdin.readline().rstrip().split())
    Commands.append(command)

commandCount = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0
endTime = 0
nowCommand = Commands.popleft()
for i in range(1, int(Commands[-1][0])+1):
    if board[snakeHead[0]][snakeHead[1]] == 2:
        pass
    board[snakeHead[0]][snakeHead[1]] = 0
    snakeHead[0] += dy[direction]
    snakeHead[1] += dx[direction]
    if board[snakeHead[0]][snakeHead[1]] == 1:
        endTime = i
        break
    board[snakeHead[0]][snakeHead[1]] = 3
    if i == int(nowCommand[0]):
        if nowCommand[1] == 'D':
            direction += 1
        elif nowCommand[1] == 'C':
            direction -= 1
        direction = direction % 4
        if Commands:
            nowCommand = Commands.popleft()
    print2D(board)
print(endTime)





