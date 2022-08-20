# 이코테 Q1 모험가 길드

n = int(input())
data = list(map(int, input().split()))
result = 0 # 그룹 수
count = 0

data.sort() #오름차순 정렬

for i in data :
    count += 1
    if count >= i :
        result += 1
        count = 0

print(result)