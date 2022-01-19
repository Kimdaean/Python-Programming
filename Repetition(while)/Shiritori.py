from inputimeout import inputimeout, TimeoutOccurred
print("START")
start=input("시작단어를 입력하세요: ")
while True:
    try:
        word=inputimeout(prompt=f"{start}: ",timeout=3)
    except:
        print("시간이 초과되었습니다!")
        break
    if start[-1]==word[0]:
        print("PASS :)")
        start=word
    else:
        print("FAIL :(")
        break
