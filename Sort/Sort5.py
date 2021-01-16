# 위에서 아래로 (500이하의 개수, 100000이하)
n = int(input())
input_arr = []
for i in range(n):
    input_arr.append(int(input()))
"""
# 기본 라이브러리 사용
input_arr.sort(reverse=True)
for i in input_arr:
    print(i, end=' ')
"""

# 계수정렬
count_arr = [0 for _ in range(max(input_arr)+1)]
for i in input_arr:
    count_arr[i] += 1
for i in range(1,len(count_arr)+1):
    if count_arr[-1*i] != 0:
        for j in range(count_arr[-1*i]):
            print(len(count_arr)-i, end=' ')

