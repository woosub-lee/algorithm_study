# 피보나치 함수
# 외부코드에서 입력을 제공받음 (https://www.acmicpc.net/problem/1003 참고)
"""
실수했던 점: 간단한 DP문제를 성공적으로 해결함

기억해야할 점: 상향식과 하향식을 모두 사용하여 풀이를 해결함
"""
call_table = [[0, 0] for i in range(41)]
call_table[0] = [1, 0]
call_table[1] = [0, 1]
# 상향식
"""
for i in range(2, 41):
    call_table[i][0] = call_table[i-1][0] + call_table[i-2][0]
    call_table[i][1] = call_table[i-1][1] + call_table[i-2][1]
for i in range(int(input())):
    target = int(input())
    print(call_table[target][0], call_table[target][1])
"""
# 하향식
def fibonacci_call_count(x):
    global call_table
    if call_table[x] != [0, 0]:
        return call_table[x]
    pre1_value = fibonacci_call_count(x-1)
    pre2_value = fibonacci_call_count(x-2)
    call_table[x][0] = pre1_value[0] + pre2_value[0]
    call_table[x][1] = pre1_value[1] + pre2_value[1]
    return call_table[x]


for i in range(int(input())):
    target = int(input())
    fibonacci_call_count(target)
    print(call_table[target][0], call_table[target][1])