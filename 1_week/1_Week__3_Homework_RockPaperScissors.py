import random

# 이긴 횟수, 경기 횟수 초기화
win_user = 0
win_com = 0
tie = 0
num = 0

# 가위바위보 게임
while(True):
    num = num + 1
    print(str(num) + "번째 경기")

# 사용자의 선택
    answer = input("가위, 바위, 보 중에 당신의 선택은?")

# 컴퓨터의 선택
    choices = ["가위", "바위", "보"]
    com_answer = random.choice(choices)

# 승패의 원리
    if answer == "가위":
        if com_answer == "가위":
            print("비겼습니다.")
            tie = tie + 1
        elif com_answer == "바위":
            print("컴퓨터가 이겼습니다.")
            win_com = win_com + 1
        else:
            print("사용자가 이겼습니다.")
            win_user = win_user + 1
    elif answer == "바위":
        if com_answer == "바위":
            print("비겼습니다.")
            tie = tie + 1
        elif com_answer == "보":
            print("컴퓨터가 이겼습니다.")
            win_com = win_com + 1
        else:
            print("사용자가 이겼습니다.")
            win_user = win_user + 1
    elif answer =="보":
        if com_answer == "보":
            print("비겼습니다.")
            tie = tie + 1
        elif com_answer == "가위":
            print("컴퓨터가 이겼습니다.")
            win_com = win_com + 1
        else:
            print("사용자가 이겼습니다.")
            win_user = win_user + 1


# 사용자가 가위, 바위, 보 중에 안골랐을 때
    else:
        print("가위, 바위, 보 낸거 맞나요?")
        break

# 승패 결정
    if win_user >= 3 and win_com < 3:
        print("축하드립니다. 당신이 이겼습니다!")
        print("사용자: " + str(win_user) + "승" + str(win_com) + "패" + str(tie) + "무")
        break
    elif win_user < 3 and win_com >= 3:
        print("안타깝네요. 컴퓨터가 이겼습니다!")
        print("컴퓨터: " + str(win_com) + "승" + str(win_user) + "패" + str(tie) + "무")
        break
