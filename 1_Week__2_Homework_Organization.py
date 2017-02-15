class Person():

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# # 기본 직급이 대리일 경우.
# class Colleague(Person):
#     position = "대리"

# 직급도 입력받도록 하기.
class Colleague(Person):
    def __init__(self, name, age, gender, position):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = position




# For Test
person_a = Person("형도", "28", "남자")
print(person_a.name)
person_b = Colleague("도형", "82", "여자", "대리")
print(person_b.position)
