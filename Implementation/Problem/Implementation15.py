# 요세푸스 문제0
# 외부코드에서 입력을 제공받음 (https://www.acmicpc.net/problem/11866 참고)
"""
실수했던 점: 인덱스 에러 발생함

기억해야할 점: stack을 이용하여 해결함
"""
import sys
n, k = map(int, input().split())
numbers = [str(i+1) for i in range(n)]
result = []
index = 0
while numbers:
    index = (index+k-1) % len(numbers)
    result.append(numbers.pop(index))
sys.stdout.write('<')
for number in result[:-1]:
    sys.stdout.write(number+', ')
sys.stdout.write(result[-1]+'>')