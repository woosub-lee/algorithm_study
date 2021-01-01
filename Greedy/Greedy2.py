#배열의 크기 숫자가 더해지는 횟수 연속될 수 있는 숫자가 정해질 때 가장 큰 수를 구하여라
n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
num1 = data[n-1]
num2 = data[n-2]
result = 0
for i in range(1,m+1):
    if k%i>0:
        result += num1
    else:
        result += num2
print(result)
