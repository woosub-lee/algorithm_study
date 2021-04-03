# 국영수
# 외부에서 입력예제 제공 (https://www.acmicpc.net/problem/10825 참고)
"""
실수했던 점: 소괄호를 여닫는데 실수를 범함

기억해야할 점: 람다 우선순위를 처음 사용해봄
"""
peopleCount = int(input())
people = []
for i in range(peopleCount):
    name, nationalLang, english, math = input().split()
    people.append([name, int(nationalLang), int(english), int(math)])
people = sorted(people, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for person in people:
    print(person[0])