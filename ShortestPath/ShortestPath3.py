"""
미래 도시
각 기업가 서로 이어져 있고 현재 방문판매원은 1번 도시에,
N개의 기업이 존재하는데, 소개팅 상대는 K번에, 목적지는 X번에 있다.
K번을 거쳐 X까지 가는 최소시간 구하기, X까지 도달할 수 없으면 -1
시간은 간선 하나 지날때 마다 +1
플루이드 워셜, 1에서 K까지의 최솟값 + K에서 X까지의 최솟값
"""
INF = 987654321  # 이어지지 않음을 표시 (거리가 무한)
Company, Edge = map(int, input().split())  # 회사의 수와 간선의 수
Edges = [[INF for i in range(Company+1)] for j in range(Company+1)]  # DP테이블

for i in range(Edge):  # 간선의 수만큼
    StartNode, EndNode = map(int, input().split())
    # 시작점 자신과의 거리는 0
    Edges[StartNode][StartNode] = 0
    # 양방향 간선
    Edges[StartNode][EndNode] = 1
    Edges[EndNode][StartNode] = 1

Destination, StopOver = map(int, input().split())  # 목적지, 경유지

# 플루이드 워셜
for current in range(1, Company+1):
    for start in range(1, Company+1):
        for end in range(1, Company+1):
            Edges[start][end] = min(Edges[start][end], Edges[start][current] + Edges[current][end])

# result: 시작점 1노드부터 경유지까지의 최단거리 + 경유지노드부터 목적지까지의 최단거리
result = Edges[1][StopOver] + Edges[StopOver][Destination]

# 출력
if result >= INF:  # 이어져있지 않으면
    print(-1)
else:
    print(result)


"""
input1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

input2
4 2
1 3
2 4
3 4
"""

"""
output1
3

output2
-1
"""
