# 이코테 Q1 모험가 길드

n = int(input())
data = list(map(int, input().split()))
result = 0
count = 0

data.sort()

for i in data :
    count += 1
    if count >= i :
        result += 1
        count = 0

print(result)