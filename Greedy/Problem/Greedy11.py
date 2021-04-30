# 소트
# 외부에서 입력을 제공받음 (https://www.acmicpc.net/problem/1071 참고)
"""
실수했던 점: pop을 popleft로 오인, 결과 리스트 순서에 영향이 있었음
기억해야할 점: deque와 리스트를 합칠 수 없으니, deque를 리스트로 만들어서 더하여야 함
"""
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
length = int(input())
numbers = deque(sorted(list(map(int, input().rstrip().split()))))
temp_numbers = []
sorted_numbers = [numbers.popleft()]
while numbers:
    now = numbers.popleft()
    if sorted_numbers[-1]+1 == now:
        temp_numbers.append(now)
    else:
        sorted_numbers.append(now)
        numbers = deque(temp_numbers+list(numbers))
        temp_numbers = []
if temp_numbers:
    for i in range(len(sorted_numbers)-1, 0, -1):
        if sorted_numbers[i] != sorted_numbers[i-1]:
            sorted_numbers = sorted_numbers[:i] + temp_numbers + sorted_numbers[i:len(sorted_numbers)]
            temp_numbers = []
            break
    if temp_numbers:
        sorted_numbers = temp_numbers + sorted_numbers
for number in sorted_numbers:
    print(str(number)+' ')
    
