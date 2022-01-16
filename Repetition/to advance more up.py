# It is a code that determines whether a pickup occurs when two numbers are input and two numbers are added.

for i in range(5):
    A=int(input("수 입력"))
    B=int(input("수 입력"))
    if (A%10)+(B%10)>=10:
        print(A,"와",B,"를 더하면 받아올림이 발생합니다.")
    else:
        print(A,"와",B,"를 더하면 받아올림이 발생하지 않습니다.")