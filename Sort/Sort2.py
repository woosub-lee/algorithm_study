# 삽입정렬 예제 (데이터가 정렬 되어 있을수록 빠름)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array = [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else:
            break

print(array)

