# 실습 5
arr = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(arr)

for i in range(4):
    for j in range(4):
        if arr[i]<arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr)

#4523 
#i<j
#00 44
#01 45 5423  
#02 52 
#03 53
#10 45 4523
#11 
#12 52
#13 53 
#20 24 2453
#21 54
#22
#23 53
#30 32
#31 34 2354
#32 45 2345 
#33

# 실습 1
sent = input()
print(sent[::-1])

# 실습 2
sent = input()  #0123456 이 다음 만큼
cri = input()   #01
count = 0
for i in range(len(sent)):
    if cri in sent[i:i+len(cri)]:
        count +=1
print(count)