# exceptions 버그 . 예외처리

# ZeroDivisionError : 0으로 나눈 에러 자체의 이름
# 1 / 0

def divide_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."


# 4 / 2
print(divide_by(4, 2))
print(divide_by(4, 0))

# 예외 만들기
# Exception 이라는 Class가 존재! 이걸 상속하자.
class EvenNumberDivisionError(Exception):
    pass
# 클래스는 언더바없이 대문자~대문자~ 이렇게 표현.
# 함수는 언더바로 사용. 파이썬 사용자끼리의 약속임!
def divide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDivisionError #에러를 일으켜야하는 상황
    else:
        return first / second

print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))
