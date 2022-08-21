# 이코테 Q2 곱하기 혹은 더하기

arr = list(map(int,input()))

result = arr[0]

for i in range(1,len(arr)) :
    n = arr[i]
    if result <=1 or n<=1 :
        result += arr[i]
    else :
        result *= arr[i]

print(result)