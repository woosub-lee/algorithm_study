# 게임
# 외부에서 입력예제 제공 (https://www.acmicpc.net/problem/1103 참고)
"""
실수했던 점:

기억해야할 점:
"""
import sys
input = sys.stdin.readline
rowCount, columnCount = map(int, input().rstrip().split())
board = []
visited = [[False for i in range(columnCount)] for j in range(rowCount)]
for i in range(rowCount):
    board.append(list(input().rstrip()))
isLoop = False
result = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def isWrong(position):
    if position[0] >= rowCount or position[0] < 0:
        return True
    if position[1] >= columnCount or position[1] < 0:
        return True
    if board[position[0]][position[1]] == 'H':
        return True
    return False


def dfs(depth, now):
    global visited
    global result
    global isLoop
    if isWrong(now):
        result = max(result, depth)
        return
    if visited[now[0]][now[1]] == True:
        isLoop = True
        return
    visited[now[0]][now[1]] = True
    for i in range(4):
        newY = (dy[i]*int(board[now[0]][now[1]])) + now[0]
        newX = (dx[i]*int(board[now[0]][now[1]])) + now[1]
        if isLoop:
            return
        dfs(depth+1, [newY, newX])
        if not isWrong([newY, newX]):
            visited[newY][newX] = False


dfs(0, [0, 0])
if isLoop:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(result))

