# 실습 1
result = 0
while True:
    num = int(input())
    if num < 0 or result > 500:
        print(result)
        break
    if num <= 100:
        result = result + num
    
# 실습 2
nums = []
for i in range(5):
    num = int(input())
    nums.append(num)
print(max(nums), min(nums))

# 실습 3
num = int(input()) # 5
for i in range(1, num+1): # 1, 2, 3, 4, 5
    for j in range(1, i+1):
        print(j, end="")
    print("")

# 실습 4
num = int(input("입력 :"))
for i in range(1, num+1):
    if num%i==0:
        print(i)

# 실습 5 
num = int(input("입력 :")) # 5 
sent = "1"
result = 1
for i in range(2, num+1): #2,3,4,5
    sent = sent + "*" + str(i)
    result = result*i
print("{}!={}={}" .format(num, sent, result))

# 실습 6
n, m = input().split()  # "27" "36"
n = int(n)  # 27
m = int(m)  # 36

divisor = []
for i in (n,m): 
    for j in range(1, int(i)+1):  # 1~27 / # 1~36
        if (int(i))%j == 0:
            divisor.append(j)  # 약수 한 리스트 안에
    
tem = list(set(divisor))  # 중복 제거 한 리스트

for a in tem:
    if a in divisor:
        divisor.remove(a)  # 공약수만

gcd = max(divisor)  # 최대공약수
lcm = n*m/gcd

print("최대공약수 : %d" %gcd)
print("최소공배수 : %d" %lcm)


            