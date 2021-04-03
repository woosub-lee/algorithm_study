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
                    dfs(depth+1, words[i], visited)
                    visited[i] = False
                    
    dfs(0, begin, visited)
    if answer == 987654321:
        return 0
    return answer
