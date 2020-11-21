#숫자 카드 게임(2중 반복문)
n,m = map(int,input().split())
result = 0
for i in range(n):
    data = list(map(int,input().split()))
    temp_arr = data[0]
    for j in range(m):
        if data[j]<temp_arr:
            temp_arr = data[j]
    if result<temp_arr:
        result = temp_arr
print(result)