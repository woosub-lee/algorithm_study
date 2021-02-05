"""
전보
N개의 도시, M개의 통로, 메세지를 보내고자 하는 도시 C
메세지는 통로로만 이동할 수 있다.
몇개의 도시가 C도시의 메세지를 받을 수 있고,
도시들이 모두 메세지를 받는 시간은 언제인가?
입력:
    N, M, C
    M만큼 반복:
        시작노드, 종료노드, 메세지의 전달 시간
"""
import heapq

INF = 987654321  # 이어져 있지 않음
City, Edge, StartCity = map(int, input().split())
Edges = [[] for i in range(City+1)]  # 간선 정보 저장을 위한 2차원 리스트
Distances = [INF for i in range(City+1)]  # 거리저장을 위한 1차원 리스트

for i in range(Edge):
    StartNode, EndNode, Distance = map(int, input().split())
    Edges[StartNode].append((EndNode, Distance))

Queue = []  # heapq를 통해 우선순위 큐로 등장
heapq.heappush(Queue, (0, StartCity))  # 튜플의 첫 원소가 우선순위(거리)
while Queue:  # Queue가 빌때 까지
    DistanceNow, Now = heapq.heappop(Queue)
    if DistanceNow > Distances[Now]:  # 최소거리가 아니면 continue
        continue
    for anotherPath in Edges[Now]:
        FinalDistance = DistanceNow + anotherPath[1]  # 최종 소요시간
        if FinalDistance < Distances[anotherPath[0]]:  # 최종 소요시간이 다른길의 최소거리보다 작으면 갱신
            Distances[anotherPath[0]] = FinalDistance
            heapq.heappush(Queue, (FinalDistance, anotherPath[0]))

# 출력
AvailableCity = len(Distances)-Distances.count(INF)
Temp = [i for i in Distances if i != INF]
if len(Temp) > 1:
    Time = max(Temp)
elif len(Temp) == 1:
    Time = Temp[0]
else:
    Time = -1
print(AvailableCity, Time)

"""
input1
3 2 1
1 2 4
1 3 2

input2
5 4 2
2 4 1
2 3 2
3 5 10
3 1 3
"""
"""
output1
2 4

output2
4 12
"""
