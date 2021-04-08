# 카드 정렬하기
# 외부에서 입력예제 제공 (https://www.acmicpc.net/submit/1715 참고)
"""
실수했던 점: 처음 heappop을 진행할때 heapify를 진행하지 않아
           입력의 처음 값이 나왔다.

기억해야할 점: heappop은 0인덱스를 출력한 후 heapify를 진행하는 것 같다.
"""
import sys
import heapq
cards = []
for i in range(int(sys.stdin.readline().rstrip())):
    cards.append(int(sys.stdin.readline().rstrip()))
answer = 0
heapq.heapify(cards)
while len(cards)>1:
    value1 = heapq.heappop(cards)
    value2 = heapq.heappop(cards)
    heapq.heappush(cards, value1+value2)
    answer += value1 + value2
sys.stdout.write(str(answer))