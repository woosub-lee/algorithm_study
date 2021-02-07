# 서로소 집합 구조
def FindParent(array, current):
    if array[current] != current:
        array[current] = FindParent(array, array[current])
    return array[current]


def UnionParent(array, element1, element2):
    element1 = FindParent(array, element1)
    element2 = FindParent(array, element2)
    if element2 > element1:
        array[element2] = element1
    else:
        array[element1] = element2


NumberOfElement, NumberOfEdge = map(int, input().split())
Elements = [i for i in range(NumberOfElement+1)]
for i in range(NumberOfEdge):
    FirstNode, SecondNode = map(int, input().split())
    UnionParent(Elements, FirstNode, SecondNode)

# 출력
print("원소가 속한 집합:", end=" ")
for i in range(1, NumberOfElement+1):
    print(FindParent(Elements, i), end=" ")
print()

print("부모 테이블:", end=" ")
for element in Elements[1:]:
    print(element, end=" ")

"""
input
6 4
1 4
2 3
2 4
5 6
"""

"""
output
원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 1 1 5 5 
"""
