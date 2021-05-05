# 36진수
# 외부코드에서 입력을 제공받음 (https://www.acmicpc.net/problem/1593 참고)
"""
실수했던 점: 모든 순열을 담아 메모리 초과가 났었다.

기억해야할 점: counter에서 순차적으로 앞의 count를 제외하였다.
"""


def alphabet_to_index(alphabet):
    if ord('a') <= ord(alphabet) <= ord('z'):
        return ord(alphabet)-ord('a')
    return ord(alphabet)-ord('A')+26


wordLength, stringLength = map(int, input().split())
word = input()
string = input()
wordCounter = [0 for i in range(52)]
stringCounter = [0 for i in range(52)]
answer = 0

for char in word:
    wordCounter[alphabet_to_index(char)] += 1

for i in range(stringLength):
    stringCounter[alphabet_to_index(string[i])] += 1
    if i > wordLength-2:
        if stringCounter == wordCounter:
            answer += 1
        stringCounter[alphabet_to_index(string[i-wordLength+1])] -= 1

print(answer)
