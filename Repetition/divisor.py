#It is a code that receives a number and obtains a divisor of the number received.

A=int(input("숫자 입력하세요: "))
li=[]
for i in range(1,A//2+1):
    if A%i==0:
        li.append(i)
li.append(A)
print(li)

#It is a code that receives two numbers and obtains the two numbers of common divisors

A=int(input("숫자 입력하세요: "))
B=int(input("숫자 입력하세요: "))
li=[]
if A>B:
    for i in range(1,B+1):
        if B%i==0 and A%i==0:
            li.append(i)
else:
    for i in range(1,A+1):
        if A%i==0 and B%i==0:
            li.append(i)
print(li)