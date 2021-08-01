# -------------
# <1> 실습 반올림

# 입력
f = open("INPUT.TXT", "w")
num = int(input())
f.write(str(num))
f.close()

#출력
s = open("OUTPUT.TXT", "w")
for i in range(-1,-4,-1):
    s.write("{} \n" .format(str(round(num, i))))
s.close()


# -------------
# <2> 실습 수 뒤집기

# 입력
f = open("INPUT.TXT", "w")

f.close()

#출력
s = open("OUTPUT.TXT", "w")

s.close()


# -------------
# <3> 역달팽이



# -------------
# <4> 지그재그
num = int(input())

for i in range(1, num*num+1 ,num): # 1, 6(1+5), 11(1+10), 16(1+15), 21
    if ((i-1) // num)%2 == 0:
        for i in range(i, i+num):
            print(i, end="")
    else:
        for i in range(i+num-1, i-1, -1):
            print(i, end="")
    print("")


# -------------
# <5> 소인수분해
num = int(input())

arr = []

i = 2
while num > 1:
    if num % i == 0:
        arr.append(i)
        num = num // i
    else:
        i = i+1


print(arr)


# -------------
# <6> 소수 판정
num = int(input())

i = 2

result = "YES"

while i < num:
    if num % i == 0:
        result = "No"
        break
    i = i + 1

print(result)



# -------------
# <7> 팔씨름 대회
win_play = int(input())

numerator = 1  # 분자
denominator = 1  # 분모

for i in range(win_play, win_play*2): # 분자
    numerator = numerator*i

for j in range(1, win_play+1):  # 분모
    denominator = denominator*j

total_case = numerator/denominator
print(total_case)


# -------------
# <8> 숫자 뱀
