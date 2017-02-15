import random

selection = input("한식/일식/중식 중 한가지를 고르세요.")

korean_food = ["경복궁","창고43","현대정"]
japanese_food = ["이춘복참치", "코코이찌방야", "텐진호르몬"]
chinese_food = ["빠오빠오", "목란", "이화원"]


if selection == "한식":
    print(random.choice(korean_food))
elif selection == "일식":
    print(random.choice(japanese_food))
elif selection == "중식":
    print(random.choice(japanese_food))
else:
    print("원하는 게 없습니다.")
