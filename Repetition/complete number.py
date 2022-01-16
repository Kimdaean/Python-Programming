#It is a code that receives a number and determines whether the number received is a complete number

A=int(input("숫자 입력하세요: "))
li=[]
for i in range(1,A//2+1):
    if A%i==0:
        li.append(i)
if sum(li)==A:
    print(A)
else :
    print("완전수 아닙니다.")