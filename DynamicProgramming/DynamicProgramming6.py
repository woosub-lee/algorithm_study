# 정수 삼각형
# 외부 소스코드에서 입력을 제공받음(https://programmers.co.kr/learn/courses/30/lessons/43105 참고)
"""
실수했던 점: 시간복잡도를 간과하고 모든 경우의 수를 다 세었다

기억해야 할점: copy를 통해 deepcopy를 사용할 수 있었다.
              더빠르게 deepcopy를 할수있는 방법은 없을까?
"""
import copy
def count_tri(triangle, counted):
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            x0 = triangle[i+1][j]+counted[i][j]
            x1 = triangle[i+1][j+1]+counted[i][j]
            if counted[i+1][j] < x0:
                counted[i+1][j] = x0
            if counted[i+1][j+1] < x1:
                counted[i+1][j+1] = x1

def solution(triangle):
    counted = copy.deepcopy(triangle)
    count_tri(triangle, counted)
    answer = max(counted[len(counted)-1])
    return answer
