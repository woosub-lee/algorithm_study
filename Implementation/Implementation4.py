# 게임 개발
n, m = map(int, input().split())
curY, curX, curD = map(int, input().split())
dirc = ['N', 'E', 'S', 'W']
dx = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
dy = {'N': -1, 'E': 0, 'S': 1, 'W': 0}
dirCount = 0
count = 1
maps = [[]]*n
for i in range(n):
    maps[i] = list(map(int, input().split()))
while True:
    maps[curY][curX] = 1
    curD -= 1
    dirCount += 1
    if curD == -1:
        curD = 3
    if maps[curY + dy[dirc[curD]]][curX + dx[dirc[curD]]] == 0:
        count += 1
        dirCount = 0
        curY += dy[dirc[curD]]
        curX += dx[dirc[curD]]
    if dirCount == 4:
        break
print(count)
