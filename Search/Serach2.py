# 이진탐색 예제
def binary_search(array, target, start, end):
    middle = (start + end) // 2
    if start > end:
        print(start, middle, end)
        return None
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        print(start, middle, end)
        return binary_search(array, target, start, middle-1)
    elif array[middle] < target:
        print(start, middle, end)
        return binary_search(array, target, middle+1, end)


array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
target = 17
result = binary_search(array, target, 0, 9)
print(result)