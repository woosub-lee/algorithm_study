# 순차탐색 예제
def sequential_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i + 1
    return -1


input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(array, target))