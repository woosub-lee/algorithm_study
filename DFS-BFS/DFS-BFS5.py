from collections import deque

n, m = map(int, input().split())
maps = []
count = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(n):
    maps.append(list(map(int, input().split())))


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if ay == -1 or ay >= n or ax == -1 or ax >= m or (ay == 0 and ax == 0):
                continue
            if maps[ay][ax] == 0:
                continue
            if maps[ay][ax] == 1:
                maps[ay][ax] = maps[y][x] + 1
                queue.append((ay,ax))
    return maps[n-1][m-1]


print(bfs(0,0))
print(maps)