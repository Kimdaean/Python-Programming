#It is a code that receives a number and finds a prime number in a number below the number received

A=int(input("숫자 입력하세요: "))
li=[]
for i in range(1,A+1):
    if A%i==0:
        li.append(i)
if len(li)==2:
    print("소수")
else:
    print("소수 아님")