# 도시 분할 계획 (최소신장트리)
def FindParent(array, current):
    if array[current] != current:
        array[current] = FindParent(array, array[current])
    return array[current]

# 간선으로 두 집을 연결
def ConnectHouses(houses, house1, house2):
    house1 = FindParent(houses, house1)
    house2 = FindParent(houses, house2)
    if house2 > house1:
        houses[house2] = house1
    else:
        houses[house1] = house2

# 사이클 판별
def isCycled(array, element1, element2):
    if FindParent(array, element1) == FindParent(array, element2):
        return True
    return False


NumberOfHouse, NumberOfRoad = map(int, input().split())
Houses = [i for i in range(NumberOfHouse+1)]
Roads = []
LongestDistance = 0
FinalDistance = 0
for i in range(NumberOfRoad):
    Node1, Node2, Distance = map(int, input().split())
    Roads.append([(Node1, Node2), Distance])
Roads = sorted(Roads, key=lambda x: x[1])
for road in Roads:
    # 부모가 같은 사이클 상태가 아니면 ConnectHouse 실행
    if not isCycled(Houses, road[0][0], road[0][1]):
        ConnectHouses(Houses, road[0][0], road[0][1])
        FinalDistance += road[1]
        if LongestDistance < road[1]:
            LongestDistance = road[1]

# 최소 비용으로 마을 두 개를 만드는 방법: 최소 신장 트리에서 가장 비용이 높은 간선을 제거!
FinalDistance -= LongestDistance
print(FinalDistance)
