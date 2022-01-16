#It is a code that receives the number of 5 subjects, calculates the average, and finds subjects with lower scores than the average.

li=[]
for i in range(5):
    A=int(input("과목 입력: "))
    li.append(A)
print("5 과목의 평균은",sum(li)/5,"입니다.")
for i in range(5):
    if li[i]<=sum(li)/5:
        print(li[i],"는 평균이하입니다.")