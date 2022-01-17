# It is a code that receives an accurate input value of an integer type from a user, obtains an average of the received input value, and outputs numbers below average among the received numbers.

li=[]
while True:
    A=input("수 입력: (종료 q)")
    if A.isnumeric(): #숫자 정상적으로 입력한 경우
        A=int(A) #문자형을 정수형로 변환
        if 0<=A<=100: #바운더리 안에 값이 입력
            li.append(A)
        else: #바운더리 밖 숫자 입력
            print("0에서 100까지만!!")
    else: #문자 섞여있을 겨우
        if A =='q':
            if li:
                avg = sum(li)/len(li)
                print("평균 >",avg)
                for i in li:
                    if i >= avg:
                        print(i,"는 평균이상")
            else:
                print("리스트가 비어있습니다.")
            break
        else:
            print("숫자만 입력하세요!")
