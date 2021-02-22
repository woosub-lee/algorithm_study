# 자물쇠와 열쇠
# 외부 소스코드에서 입력을 제공받음 (https://programmers.co.kr/learn/courses/30/lessons/60059 참조)
"""
실수했던점: 'key의 사이즈는 항상 lock의 사이즈 이하이다.' 를 보지 못하여
           ExpendedLock 구성 및 로직구성에 어려움을 겪음
           다음부터 조건 더욱 꼼꼼히 체크할 것

기억해야할 점: 입력의 크기가 작아서 완전탐색으로 진행해도 충분히 해결할 수 있었음
"""

def rotateKey(key):
    result = []
    for i in range(len(key) - 1, -1, -1):
        row = list(map(lambda x: x[i], key))
        result.append(row)
    return result


def Check(lock, lockSize):
    for i in range(lockSize):
        for j in range(lockSize):
            if lock[lockSize + i][lockSize + j] != 1:
                return False
    return True


def extendLock(lock):
    SizeOfLock = len(lock)
    ExtendedLock = [[0 for i in range(SizeOfLock * 3)] for j in range(SizeOfLock * 3)]
    for i in range(SizeOfLock):
        for j in range(SizeOfLock):
            ExtendedLock[SizeOfLock + i][SizeOfLock + j] += lock[i][j]
    return ExtendedLock


def solution(key, lock):
    SizeOfLock = len(lock)
    SizeOfKey = len(key)
    ExtendedLock = extendLock(lock)
    for rotation in range(4):
        for i in range(1, SizeOfLock * 2):
            for j in range(1, SizeOfLock * 2):
                for y in range(SizeOfKey):
                    for x in range(SizeOfKey):
                        ExtendedLock[i + y][j + x] += key[y][x]
                if Check(ExtendedLock, SizeOfLock):
                    return True
                else:
                    for y in range(SizeOfKey):
                        for x in range(SizeOfKey):
                            ExtendedLock[i + y][j + x] -= key[y][x]
        key = rotateKey(key)
    return False