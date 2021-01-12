# 선택정렬 예제 (On^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    index = i
    for j in range(i+1, len(array)):
        if array[index] > array[j]:
            index = j
    array[i], array[index] = array[index], array[i]

print(array)
