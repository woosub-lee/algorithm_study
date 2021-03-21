# 소수 찾기
# 외부 소스 코드에서 입력을 제공받음
"""
실수했던 점: X

기억해야할 점: 순열을 만들어내는 permutation을 통해 구현해내었다.
"""
import math
from itertools import permutations
def isPrime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numberCases = []
    result = set()
    for i in range(1, len(numbers)+1):
        numberCases.append(list(permutations(numbers, i)))
    for cases in numberCases:
        for case in cases:
            temp = "".join(case)
            if isPrime(int(temp)):
                result.add(int(temp))
    answer = len(result)
    return answer