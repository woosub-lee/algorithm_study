# 문자열 뒤집기
def DataZip(data):
    ZippedData = [data[0]]
    for d in data[1:]:
        if d != ZippedData[-1]:
            ZippedData.append(d)
    return ZippedData


OriginalData = list(input())
Data = DataZip(OriginalData)
print(Data)
NumberOfReverse = min(Data.count('0'), Data.count('1'))
print(NumberOfReverse)
