su = 0
while True:
    print('-'*4,"Menu",'-'*4)
    print("1.콜라 / 300")
    print("2.사이다 / 300")
    print("3.커피 / 200")
    print("4. 돈 넣기")
    print("5. 잔돈 반환")
    print("6. 종료")
    print('-'*20)
    print("현재 금액",su)
    menu=int(input("메뉴 선택: "))
    if menu == 4:
        money=int(input("돈을 넣어주세요: "))
        su+=money
    elif menu == 1:
        if (money>=300):
            su -= 300
            print("\n콜라 맛있게 드세요")
        else:
            print("\n금액이 부족합니다.")
    elif menu == 2:
        if (money>=300):
            su -= 300
            print("\n사이다 맛있게 드세요")
        else:
            print("\n금액이 부족합니다.")
    elif menu == 3:
        if (money>=200):
            su -= 200
            print("\n커피 맛있게 드세요")
        else:
            print("\n금액이 부족합니다.")
    elif menu == 5:
        su = 0
        print("\n잔돈이 반환됩니다!")
        money = 0
    elif menu == 6:
        break
    else:
        print("\n입력 오류")
