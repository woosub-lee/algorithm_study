# 계수 정렬 예제
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def count_sort(array):
    max_num = max(array)
    result = []
    for i in range(max_num+1):
        count = array.count(i)
        for j in range(count):
            result.append(i)
    return result


def in_book(array):
    count = [0] * (max(array)+1)
    result = []
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
    return result


print(count_sort(array))
print(in_book(array))
