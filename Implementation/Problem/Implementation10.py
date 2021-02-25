# 기둥과 보 설치
# 외부소스코드에서 입력을 제공받습니다. n, build_frame (https://programmers.co.kr/learn/courses/30/lessons/60061 참조)
"""
실수했던점: 보드에 일일이 건물 정보를 기록할 필요가 없었음
          보 설치의 조건을 잘못 이해하여 어려움이 있었음

기억해야할 점: 입력의 크기가 1000이고 실행 제한시간이 5초라 O(N^3)로 풀 수 있었음
             시간복잡도를 줄일 수 있는 방안이 있는지 고민해봐야 될듯함
"""
def isRight(buildings):
    for building in buildings:
        positionX, positionY, buildingKind = building
        # 기둥
        if buildingKind == 0:
            if positionY == 0:
                continue
            Targets = [[positionX-1, positionY, 1],
                       [positionX, positionY, 1],
                       [positionX, positionY-1, 0]
                      ]
            if Targets[0] in buildings or Targets[1] in buildings or Targets[2] in buildings:
                continue
            return False
        # 보
        else:
            Targets = [[positionX-1, positionY, 1],
                       [positionX+1, positionY, 1],
                       [positionX, positionY-1, 0],
                       [positionX+1, positionY-1, 0]
                      ]
            if (Targets[0] in buildings and Targets[1] in buildings) or Targets[2] in buildings or Targets[3] in buildings:
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for command in build_frame:
        # 삭제
        if command[3] == 0:
            answer.remove(command[:-1])
            if not isRight(answer):
                answer.append(command[:-1])
        # 설치
        else:
            answer.append(command[:-1])
            if not isRight(answer):
                answer.remove(command[:-1])
    answer.sort()
    return answer