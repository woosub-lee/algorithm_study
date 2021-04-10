# 실패율
# 외부에서 입력예제 제공 (https://programmers.co.kr/learn/courses/30/lessons/42889 참고)
"""
실수했던 점: N+1의 의미를 혼동하여 작성함

기억해야할 점: 계수정렬을 사용하여 풀수있었다.
"""
from fractions import Fraction
def solution(N, stages):
    counter = [0 for i in range(N+2)]
    failOfStages = [[0, i] for i in range(N+2)]
    for stage in stages:
        counter[stage] += 1
    nowPeople = counter[N+1]
    for i in range(N, 0, -1):
        nowPeople += counter[i]
        if nowPeople != 0:
            failOfStages[i][0] = Fraction(counter[i], nowPeople)
    failOfStages = sorted(failOfStages[1:-1], key=lambda x: (-x[0], x[1]))
    return [stage[1] for stage in failOfStages]