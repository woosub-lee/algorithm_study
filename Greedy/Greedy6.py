# 곱하기 혹은 더하기
# 가장큰 수 만들기
# 기존 연산과 달리 연산기호의 우선 순위 존재 X
def isMultiplication(elements):
    if elements[0] == 0 or elements[0] == 1:
        return False
    elif elements[1] == 0 or elements[1] == 1:
        return False
    return True


Datas = list(map(int, list(input())))
while len(Datas) != 1:
    Elements = [Datas.pop(0), Datas[0]]
    if isMultiplication(Elements):
        Datas[0] *= Elements[0]
    else:
        Datas[0] += Elements[0]
print(Datas[0])


