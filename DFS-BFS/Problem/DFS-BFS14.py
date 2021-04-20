# 게임
# 외부에서 입력예제 제공 (https://www.acmicpc.net/problem/1103 참고)
"""
실수했던 점: dfs를 성공적으로 구현했으나, 다이나믹 프로그래밍을 고려하지 못하고 시간초과
    
기억해야할 점: DP 공부 요망
"""
import sys
input = sys.stdin.readline
rowCount, columnCount = map(int, input().rstrip().split())
board = []
visited = [[False for i in range(columnCount)] for j in range(rowCount)]
memo = [[-1 for i in range(columnCount)] for j in range(rowCount)]
for i in range(rowCount):
    board.append(list(input().rstrip()))
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


def dfs(nowY, nowX):
    global visited
    if isWrong([nowY, nowX]):
        return 0
    if visited[nowY][nowX]:
        sys.stdout.write('-1')
        exit(0)
    if not memo[nowY][nowX] == -1:
        return memo[nowY][nowX]
    visited[nowY][nowX] = True
    for i in range(4):
        newY = (dy[i]*int(board[nowY][nowX])) + nowY
        newX = (dx[i]*int(board[nowY][nowX])) + nowX
        memo[nowY][nowX] = max(memo[nowY][nowX], dfs(newY, newX)+1)
    visited[nowY][nowX] = False
    return memo[nowY][nowX]



sys.stdout.write(str(dfs(0, 0)))

