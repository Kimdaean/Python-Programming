birthday = int(input("생년월일을 입력하세요: "))
year = birthday//10000
month = birthday%10000//100 #birthdy//100%100
day = birthday%100
print(year)
print(month)
print(day)
