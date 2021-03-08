# 감시 피하기
# 외부에서 입력을 제공받음 (https://www.acmicpc.net/problem/18428 참고)
"""
실수했던 점: check함수의 반복문에서 인덱스 실수를 했었다.

기억해야할 점: 재귀적으로 dfs를 구현해냈다.
"""


from sys import stdin
boardSize = int(input())
board = []
mountedBoard = [[0 for i in range(boardSize)] for j in range(boardSize)]
isSafe = False
for i in range(boardSize):
    board.append(list(stdin.readline().rstrip().split()))

def check(board, y, x):
  for i in range(y-1, -1, -1):
    if board[i][x] == 'O':
      break
    if board[i][x] == 'S':
      return False
  for i in range(y+1, len(board)):
    if board[i][x] == 'O':
      break
    if board[i][x] == 'S':
      return False
  for j in range(x-1, -1, -1):
    if board[y][j] == 'O':
      break
    if board[y][j] == 'S':
      return False
  for j in range(x+1, len(board)):
    if board[y][j] == 'O':
      break
    if board[y][j] == 'S':
      return False
  return True

def dfs(count):
  global isSafe
  if count == 3:
    for y in range(boardSize):
      for x in range(boardSize):
        mountedBoard[y][x] = board[y][x]
    for y in range(boardSize):
      for x in range(boardSize):
        if mountedBoard[y][x] == 'T':
          if check(mountedBoard, y, x):
            continue
          else:
            return
    isSafe = True
    return
  for i in range(boardSize):
    for j in range(boardSize):
      if board[i][j] == 'X':
        board[i][j] = 'O'
        dfs(count+1)
        board[i][j] = 'X'

dfs(0)
if isSafe:
  print('YES')
else:
  print('NO')
