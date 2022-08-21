# 이코테 Q2 곱하기 혹은 더하기

arr = list(map(int,input())) #문자열 입력받기

result = arr[0] #첫 번째 숫자 지정

for i in range(1,len(arr)) : #첫 번째 숫자는 이미 지정했으므로 반복문은 arr[1]부터 시작
    n = arr[i]
    if result <=1 or n<=1 : # 두 숫자 중 하나라도 0 또는 1이면 + 연산 사용
        result += n
    else :
        result *= n

print(result)