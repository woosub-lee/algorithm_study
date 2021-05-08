# 집합의 표현
# 외부코드에서 입력을 제공받음 (https://www.acmicpc.net/problem/1717 참고)
"""
실수했던 점: 단순 입력의 크기가 너무 많아 복잡도와 상관없이 시간초과가 발생하였다.
           재귀 함수의 깊이 제한이 걸렸었다.

기억해야할 점: sys.setrecursionlimit로 재귀제한 해제
             sys.stdin.readline으로 입력시간 최소화
"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def find_first_element(element):
    global sets
    if element != sets[element]:
        sets[element] = find_first_element(sets[element])
    return sets[element]


def union_elements(element1, element2):
    global sets
    new_element1 = find_first_element(element1)
    new_element2 = find_first_element(element2)
    if new_element1 < new_element2:
        sets[new_element2] = new_element1
    else:
        sets[new_element1] = new_element2


element_count, command_count = map(int, input().rstrip().split())
sets = [i for i in range(element_count+1)]
for i in range(command_count):
    command_kind, element1, element2 = map(int, input().rstrip().split())
    if command_kind == 0:
        union_elements(element1, element2)
    else:
        if find_first_element(element1) == find_first_element(element2):
            print('YES')
        else:
            print('NO')