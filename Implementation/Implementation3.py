# 왕실의 나이트
curPlace = list(input())
dicY = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
curX = dicY[curPlace[0]]
curY = int(curPlace[1])
moveX = [1, 1, -1, -1, 2, 2, -2, -2]
moveY = [2, -2, 2, -2, 1, -1, 1, -1]
result = 0
for i in range(8):
    if curX + moveX[i] > 0 and curY + moveY[i] > 0:
        result += 1
print(result)