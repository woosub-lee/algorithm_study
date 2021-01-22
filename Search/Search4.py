# 떡볶이 떡 만들기
"""
재귀 방식
def bSearch(array, target, start, end, result):
    if start > end:
        return result
    mid = (start+end)//2
    count = 0
    for args in array:
        if args - mid > 0:
            count += args - mid
    if count < target:
        return bSearch(array, target, start, mid-1, result)
    elif count > target:
        return bSearch(array, target, mid+1, end, mid)
    elif count == target:
        return mid

n, m = map(int, input().split())
array = list(map(int, input().split()))
print(bSearch(array, m, 0, max(array), 0))
"""


# 반복문 이용
n, m = map(int, input().split())
array = list(map(int, input().split()))
result = 0
start, end = 0, max(array)
while start <= end:
    count = 0
    mid = (start+end)//2
    for args in array:
        if args - mid > 0:
            count += args - mid
    if count < m:
        end = mid-1
    if count >= m:
        start = mid+1
        result = mid
print(result)
