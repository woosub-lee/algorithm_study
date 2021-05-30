# N-Queen
# 외부코드에서 입력을 제공받음 (https://www.acmicpc.net/problem/9663 참고)
"""
실수했던 점: 시간복잡도를 고려하지 않아서 브루트포스를 사용함

기억해야할 점: 백트래킹을 사용하여 해결함
"""
UNSET = 100
answer = 0
boardSize = int(input())
board = [UNSET for _ in range(boardSize+1)]


def isRight(cIndex):
    for i in range(1, cIndex):
        if board[i] == board[cIndex]:
            return False
        if (cIndex - i) == abs(board[cIndex] - board[i]):
            return False
    return True


def nQueen(cIndex):
    global answer
    global board
    if cIndex == boardSize+1:
        answer += 1
        return
    for i in range(1, boardSize+1):
        board[cIndex] = i
        if isRight(cIndex):
            nQueen(cIndex+1)


nQueen(1)
print(answer)