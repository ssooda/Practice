# 실습 7
# i,j
# 1 3 5 7 9 (2n-1) ceil(2n-1/2) 
# 1 -> 0
# 2 -> 101
# 3 -> 21012 
# 4 -> 3210123
# 1,1

# 1,1 / 1,1 / 1,1
# 2,0 / 2,3 / 2,0 7-4 4num-1
# 3,1 / 3,1 / 3,1 7-6

# 1,2 / 1,1 / 1,2
# 2,1 / 2,3 / 2,1
# 3,0 / 3,5 / 3,0 11-6
# 4,1 / 4,3 / 4,1 11-8 
# 5,2 / 5,1 / 5,2 11-10

# 1,3 / 1,1 / 1,3
# 2,2 / 2,3 / 2,2
# 3,1 / 3,5 / 3,1
# 4,0 / 4,7 / 4,0 15-8
# 5,1 / 5,5 / 5,1 15-10(2*i)
# 6,2 / 6,3 / 6,2 15-12
# 7,3 / 7,1 / 7,3 15-1
from math import ceil
num = int(input())
for i in range(1,2*num):
    if i <= ceil((2*num-1)/2):
        print(" "*(num-i) + "*"*(2*i-1) +" "*(num-i))
    else:
        print(" "*(i-num) + "*"*((4*num-1)-2*i) + " "*(i-num))


# 실습 1
arr = list(map(int, input().split()))
avg = sum(arr)/len(arr)
for i in arr:
    if avg < i:
        print(i)
    
# 실습 2
arr = list(map(int, input().split()))
result = {}
for i in arr:
    if i in result:
        result[i] = result[i]+"*"
    else:
        result[i] = "*"

for i in range(1,4):
    print("{}:{}" .format(i, result[i]))

# 실습 3
arr = list(map(int, input().split()))
for i in range(2):
    max_num = max(arr)
    print(max_num)
    arr.remove(max_num)

# 실습 4
arr = list(map(int, input().split()))
point = int(input())
result = []
for i in range(len(arr)):
    if arr[i] == point:
        result.append(i)
if not result:
    result = "None!"
print(result)

# 실습 5
arr = list(map(int, input().split()))
print(sorted(arr))
