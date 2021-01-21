# 부품 찾기

def bSearch(array, target, start, end):
    if start > end:
        return False
    mid = (start+end)//2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return bSearch(array, target, start, mid-1)
    elif array[mid] < target:
        return bSearch(array, target, mid+1, end)


def cSort(array):
    count = [0 for _ in range(max(array)+1)]
    for args in array:
        count[args] += 1
    return count

store = int(input())
stock = list(map(int, input().split()))
customer = int(input())
require = list(map(int, input().split()))
# 이진탐색 이용
stock.sort()
print("binary Search")
for args in require:
    if bSearch(stock, args, 0, store-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
print("")
# 계수 정렬 이용
print("count Sort")
for args in require:
    array = cSort(stock)
    if args <= len(array) - 1:
        if array[args] > 0:
            array[args] -= 1
            print('yes', end=' ')
        else:
            print('no', end=' ')
    else:
        print('no', end=' ')
