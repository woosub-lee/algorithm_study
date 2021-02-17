# 문자열 뒤집기
"""
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
"""
StrData = input()
NumberOfCase0 = 0
NumberOfCase1 = 0
NumberOfReverse = 0
for i in range(1, len(StrData)):
    if StrData[i-1] != StrData[i]:
        if StrData[i] == '1':
            NumberOfCase0 += 1
        else:
            NumberOfCase1 += 1

NumberOfReverse = min(NumberOfCase0, NumberOfCase1)
print(NumberOfReverse)



