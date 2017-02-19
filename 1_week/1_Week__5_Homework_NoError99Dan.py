def gugudan():

    try:
        dan = int(input("몇 단을 출력하시겠습니까"))
        if dan>1 and dan<10:
            for num in range(1,10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            print("2에서 9사이의 숫자만 입력해주세요.")
            gugudan() # 재귀함수

# input에 문자가 껴서 ValueError가 발생한다면,
    except ValueError:
        print("2에서 9사이의 숫자만 입력해주세요.")
        gugudan() #재귀함수

# 함수 실행
gugudan()
