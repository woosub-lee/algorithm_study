# 플로이드 워셜 알고리즘 예제 O(N^2)
INF = 987654321  # not connect
node = int(input())  # 노드의 개수
edge = int(input())  # 간선의 개수
DP = [[INF for i in range(node+1)] for j in range(node+1)]  # DP 테이블
for i in range(edge):
    start, end, distance = map(int, input().split())
    DP[start][start] = 0  # 자신과의 거리는 0
    DP[start][end] = distance  # 자신과의 거리를 간선이 가르키는 노드가 해당되는 DP에 저장
for i in range(1, node+1):  # i번 노드를 거쳐가는 노드들 중에서
    for j in range(1, node+1):  # 첫 번째 노드 선택 (1node)
        for k in range(1, node+1):  # 두 번째 노드 선택 (2node)
            DP[j][k] = min(DP[j][k], DP[j][i] + DP[i][k])
            """
            '현재 최단거리'와 '1node에서 i번 노드, i번 노드에서 2node로 가는 거리의 합을 더한 것' 중에 작은 것을 DP테이블에 저장
            3단 반복문 O(N^3)
            """

# 출력
for i in range(1, node+1):
    for j in range(1, node+1):
        if i == j:
            continue
        print(i, '번 노드에서 ', j, '번 노드까지의 최단거리:', end=' ')
        if DP[i][j] == INF:
            print('not_connected')
        else:
            print(DP[i][j])
    print()
"""
input
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

output
1 번 노드에서  2 번 노드까지의 최단거리: 4
1 번 노드에서  3 번 노드까지의 최단거리: 8
1 번 노드에서  4 번 노드까지의 최단거리: 6

2 번 노드에서  1 번 노드까지의 최단거리: 3
2 번 노드에서  3 번 노드까지의 최단거리: 7
2 번 노드에서  4 번 노드까지의 최단거리: 9

3 번 노드에서  1 번 노드까지의 최단거리: 5
3 번 노드에서  2 번 노드까지의 최단거리: 9
3 번 노드에서  4 번 노드까지의 최단거리: 4

4 번 노드에서  1 번 노드까지의 최단거리: 7
4 번 노드에서  2 번 노드까지의 최단거리: 11
4 번 노드에서  3 번 노드까지의 최단거리: 2
"""
