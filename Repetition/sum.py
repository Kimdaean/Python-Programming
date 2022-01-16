#Receive the number, separate even and odd numbers from the number below the number received, and calculate the sum of even and odd numbers separately

A=int(input("수 입력: "))
sum1=0
sum2=0
for i in range(1,A+1):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
print(sum1)
print(sum2)