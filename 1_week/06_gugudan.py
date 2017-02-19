# # my turn
# dan = input("몇 단을 출력하시겠습니까? ")
# for num in range(1,10):
#     print(dan + "*" + str(num) + "=" + str(int(dan)*num))


# imagineer's turn
# 1) 사용자로부터 몇 단을 출력할 지 받을 것.
# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것.

dan=int(input("몇 단을 출력하시겠습니까?? "))
# input 데이터는 str로 받는다. 고로 int로 바꿔줌.
# for num in range(1,10):
#     print("{} * {} = {}".format(dan, num, dan * num))


if dan>1 and dan<10:
    for num in range(1,10):
        print("{} * {} = {}".format(dan, num, dan * num))
else:
    print("2~9사이 숫자만 넣어주세요")
