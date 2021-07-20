# 실습 1
print("생일입력")

month = input("입력 월: ")
date = input("입력 일: ")

print("생일은 {0}월 {1}일 입니다." .format(month, date))

# 실습 2
print("2"*6) 
print("2    2")
print("2    2") # 여기를 어떻게 간단하게 바꿀까, 대칭?
print("2"*6)

# 실습 3
print("생일 입력")
birth = input("입력 월 일:")
birth = birth.split(" ")
print("생일은 {}월 {}일 입니다." .format(birth[0], birth[1]))

# 실습 4
choice = input("정수 입력: ")
print(choice*6)
print("{0}    {0}" .format(choice))
print("{0}    {0}" .format(choice))
print(choice*6)

# 실습 1
time = int(input())
second = (time%60)
minute = (time//60)%60
hour = (time//60)//60
print("{}:{}:{}" .format(hour, minute, second))

# 실습 2
number = input()
result = False
if (20<=int(number)) & (int(number)<=30):
    result = True
print(False)

# 실습 3
degree = input()
result = "실내활동" 
if (0 <= degree) & (degree<=40) :
    resutl = "실외활동"
print(result)

# 실습 4
number = input()
number = number.split(" ")
result = int(number[0])
if result < int(number[1]):
    result = int(number[1])
print(result)

# 실습 5
number = input()
number = number.split(" ")
number.sort()
result = None
if int(number[0])**2 == int(number[1]):
    result = ("{0}*{0}={1}" .format(number[0], number[1]))
print(result)

# 실습 6
year = int(input())
result = "윤년"
if (year%4 != 0) or ((year%100 == 0) and (year%400 != 0)):
    result = "평년"
print("{}년은 {}입니다." .format(year, result))

