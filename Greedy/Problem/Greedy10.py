import heapq
# 별도의 입력 제공코드가 존재함 (https://programmers.co.kr/learn/courses/30/lessons/42891 참조)
def solution(food_times, k):
    answer = -1
    if sum(food_times) > k:

        food_times = [(food_times[i], i + 1) for i in range(len(food_times))]
        Queue = []
        preFood = 0

        for food in food_times:
            heapq.heappush(Queue, food)

        while Queue:
            CurrentFood = heapq.heappop(Queue)
            CurrentCycle = (len(Queue) + 1) * (CurrentFood[0] - preFood)
            if k < CurrentCycle:
                heapq.heappush(Queue, CurrentFood)
                break
            k -= CurrentCycle
            preFood = CurrentFood[0]

        Queue = sorted(Queue, key=lambda x: x[1])
        answer = Queue[k % len(Queue)][1]
    return answer


print(solution([3, 1, 2], 5))
