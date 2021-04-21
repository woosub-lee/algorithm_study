# N-Queen
# 외부에서 입력예제 제공 (https://programmers.co.kr/learn/courses/30/lessons/1295 참고)
"""
실수했던 점:

기억해야할 점:
"""
from collections import deque
def solution(n):
    answer = 0
    rows = [-1 for i in range(n)]
    diagonals_1 = {i:deque([]) for i in range(2*n+1)}
    diagonals_2 = {i:deque([]) for i in range(1-n, n)}
    visited = [False for i in range(n)]
    def isRight():
        for i in range(2*n+1):
            diagonal = diagonals_1[i]
            if len(diagonal) > 1:
                return False
        for i in range(1-n, n):
            diagonal = diagonals_2[i]
            if len(diagonal) > 1:
                return False
        return True
    def dfs(depth):
        nonlocal rows
        nonlocal answer
        if depth == n:
            if isRight():
                answer += 1
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                rows[depth] = i
                diagonals_1[depth+i].append(0)
                diagonals_2[i-depth].append(0)
                dfs(depth+1)
                visited[i] = False
                diagonals_1[depth+i].popleft()
                diagonals_2[i-depth].popleft()
    dfs(0)
    return answer