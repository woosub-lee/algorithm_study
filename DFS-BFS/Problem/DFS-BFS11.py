# 단어변환
# 외부코드에서 입력을 제공받음 (https://programmers.co.kr/learn/courses/30/lessons/43163 참고)
"""
실수했던 점: target 대신 예제로 주어지는 'cog'를 써버리고 말았다.

기억해야할 점: dfs를 성공적으로 구현해냄
            isRight함수로 인해 문자열에서 문자가 하나만 다른 단어를 구해내기 쉬웠음
"""

def isRight(word1, word2):
    result = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if result:
                return False
            else:
                result = True
    return result


def solution(begin, target, words):
    visited = [False for i in range(len(words))]
    answer = 987654321
    if not target in words:
        return 0
    if begin in words:
        visited[words.index(begin)] = True

    def dfs(depth, word, visited):
        nonlocal answer
        if word == target:
            answer = min(answer, depth)
            return
        for i in range(len(words)):
            if visited[i] == False:
                if isRight(word, words[i]):
                    visited[i] = True
                    dfs(depth + 1, words[i], visited)
                    visited[i] = False

    dfs(0, begin, visited)
    if answer == 987654321:
        return 0
    return answer