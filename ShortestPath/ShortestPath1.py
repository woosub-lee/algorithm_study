# 다익스트라 알고리즘 예제
"""
우선순위 큐: 우선순위가 높은 데이터를 먼저 삭제
큐: 먼저 들어온 데이터를 먼저 삭제
스택: 제일 나중에 들어온 데이터를 먼저 삭제
"""
import heapq  # 우선순위 큐
INF = 987654321  # 무한, 노드가 이어지지 않음을 뜻함
n, m = map(int, input().split())  # n:노드의 수, m:간선의 수
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # 자신, 상대, 거리
    graph[a].append([b, c])  # 그래프 배열의 자신의 노드에 상대노드와 그 거리를 삽입


def dijkstra(start):
    q = []  # 우선순위 큐: 최소힙
    heapq.heappush(q, (0, start))  # heapq: 튜플의 첫 원소를 우선순위
    distance[start] = 0  # 자신의 노드이므로 거리는 0
    while q:  # q(우선순위 큐)의 원소가 존재하는 동안
        dist, now = heapq.heappop(q)  # 거리, 현재 노드
        if distance[now] < dist:  # 최소거리가 아니면 continue
            continue
        for i in graph[now]:
            # 최종비용: 현재노드와의 거리와 현재노드와 연결된 노드의 거리의 합
            # 예를 들어 1노드와 3노의 거리: 1노드 3노드의 직선간선의 거리, 혹은 "2노드에서 1노드의 거리 + 2노드에서 3노드의 거리"
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 새로 계산한 거리가 짧은 거리이면 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)  # input 참조, start = 1, 1을 시작점으로 하는 다익스트라 알고리즘
for i in range(1, n + 1):
    if distance[i] == INF:  # 1노드와의 연결이 없으면 "INF" 출력
        print(i, '노드와는 연결되어 있지 않습니다.')
    elif distance[i] == 0:  # 시작노드 출력 : 예시 input은 1노드
        print('시작점은', i, '노드 입니다.')
    else:
        print(i, '노드와의 최단거리:', distance[i])  # 1노드와 연결 되어있을시 최단거리 출력

"""
input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
