# 메모제이션 기법 예제(피보나치 수열)
def fibo(array, number):
    if number == 1 or number == 2:
        return 1
    if array[number] != 0:
        return array[number]
    array[number] = fibo(array, number-1) + fibo(array, number-2)
    return array[number]


n = int(input())
memory = [0 for _ in range(n+1)]
print(fibo(memory, n))
