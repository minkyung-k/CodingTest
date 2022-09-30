# 이코테 Q5 볼링공 고르기

n, m = map(int, input().split())

k = list(map(int, input().split()))

count = 0

for i in range(len(k)) :
   for j in range(i,len(k)) : 
    if k[i] != k[j] :
        count += 1


print(count)