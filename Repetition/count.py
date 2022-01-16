#It is a code that receives a number and calculates the number of multiples of 3 from the number below the number received.

A=int(input("수 입력: "))
cnt=0
for i in range(1,A+1):
    if(i%3==0):
        print(i)
        cnt+=1
print(cnt)

#It is a code that receives a number, calculates the number of multiples of 2, and outputs a multiple of 2 in the number below the number received.

A=int(input("수 입력: "))
cnt=0
for i in range(1,A+1):
    if(i%2==0):
        cnt+=1
        print(i)
print(cnt)

#It is a code that receives a number and calculates the sum of multiples of 7 in the number below the number received.

A=int(input("수 입력: "))
sum=0
for i in range(1,A+1):
    if i%7==0:
        sum+=i
print(sum)

#It is a code that receives a number and calculates the difference between the number of multiples of 3 and the number of multiples of 5 in the number below the number received.

A=int(input("수 입력: "))
cnt3=0
cnt5=0
for i in range(1,A+1):
    if i%3==0:
        cnt3+=1
    if i%5==0:
        cnt5+=1
print(cnt3-cnt5)