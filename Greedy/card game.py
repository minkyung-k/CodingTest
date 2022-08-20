#숫자 카드 게임 - 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

#min 함수 이용하는 방법
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

#2중 반복문 이용하는 방법
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    result = max(result,min_value)

print(result)