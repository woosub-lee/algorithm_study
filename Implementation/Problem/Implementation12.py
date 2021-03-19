# 괄호 변환
# 외부 소스 코드에서 입력을 제공받음
"""
실수했던 점: isRight 함수 구현에 bracketCount를 세는것에 실수가 있었다.

기억해야할 점: 재귀함수로 구현했던 것이 인상깊었다.
"""
def balanceIndex(w):
    bracketCount = 0
    for i in range(len(w)):
        if w[i] == '(':
            bracketCount += 1
        else:
            bracketCount -= 1
        if bracketCount == 0:
            return i
    return 0


def isRight(u):
    bracketCount = 0
    for i in range(len(u)):
        if u[i] == '(':
            bracketCount += 1
        else:
            bracketCount -= 1
        if bracketCount<0:
            return False
    return True


def solution(p):
    if p == '':
        return ''
    answer = ''
    index = balanceIndex(p)
    u = p[:index+1]
    v = p[index+1:]
    if isRight(u):
        answer += u + solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('
        return temp
    return answer
