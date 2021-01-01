# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 돈의 최소 개수
money = [500, 100, 50, 10]
count = 0
n = int(input())
for i in money:
    count += n // i
    n %= i
print(count)
