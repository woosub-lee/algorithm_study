# 상하좌우
n = int(input())
plans = input().split()
curX, curY = 1, 1

# R L U D
xDic = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
yDic = {'R': 0, 'L': 0, 'U': -1, 'D': 1}

for i in range(len(plans)):
    if curX + xDic[plans[i]] > 0:
        curX += xDic[plans[i]]
    if curY + yDic[plans[i]] > 0:
        curY += yDic[plans[i]]
print(curY, curX)