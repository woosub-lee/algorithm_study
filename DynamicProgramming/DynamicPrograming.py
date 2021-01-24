# 다이나믹프로그래밍 예제(피보나치 수열)
def fiboTD(array, number):  # 탑다운
    if number == 1 or number == 2:
        return 1
    if array[number] != 0:
        return array[number]
    array[number] = fiboTD(array, number-1) + fiboTD(array, number-2)
    return array[number]


def fiboBU(array, number):  # 보텀업
    array[1], array[2] = 1, 1
    if number > 2:
        for i in range(3, number+1):
            array[i] = array[i-1] + array[i-2]
        return array[i]
    else:
        return array[number]

n = int(input())
memoryTD = [0 for _ in range(n+2)]  # 탑다운 방식의 메모제이션 기법을 위한 리스트
memoryBU = [0 for _ in range(n+2)]  # 보텀업 방식의 DP테이블
print(fiboTD(memoryTD, n))
print(fiboBU(memoryBU, n))
