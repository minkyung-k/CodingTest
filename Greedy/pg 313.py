# 이코테 Q3 문자열 뒤집기

data = input()
count_0 = 0
count_1 = 0

first = data[0]

if first == '0' :
    count_0 += 1
else :
    count_1 += 1

for i in range(1,(len(data)-1)) :
    if data[i] != data[i+1] :
        if data[i+1] == '0' :
            count_0 += 1
        else :
            count_1 += 1

print(min(count_0,count_1))