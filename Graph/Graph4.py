# 위상정렬
from collections import deque
NumberOfNode = int(input())
NumberOfEdge = int(input())
SortedNodes = []
Queue = deque()
InDegree = [0 for i in range(NumberOfNode+1)]  # 진입차수 리스트
Edges = [[] for i in range(NumberOfNode+1)]
# 방향그래프 이므로 출발노드, 도착노드를 구별
for i in range(NumberOfEdge):
    StartNode, EndNode = map(int, input().split())
    Edges[StartNode].append(EndNode)
    InDegree[EndNode] += 1

for i in range(NumberOfNode):
    if InDegree[i] == 0:
        Queue.append(i)
# 큐가 빌때까지 진입차수 순으로 popleft
while Queue:
    Current = Queue.popleft()
    SortedNodes.append(Current)
    for i in Edges[Current]:
        InDegree[i] -= 1
        if InDegree[i] == 0:
            Queue.append(i)

print(SortedNodes[1:])
"""
input
7
8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
"""
output
[1, 2, 5, 3, 6, 4, 7]
"""
