# # List []
# print("list")
# list_a = [1, 2, 3]
# print(list_a)
# print(type([1, 2, 3]))
# # index는 0부터 시작.
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# # slice - list를 자르다. 마지막 index는 불포함!
# print(list_a[0:2])
# # append
# list_a.append(4)
# print(list_a)
# list_a.remove(3)
# print(list_a)
# list_a.clear()
# print(list_a)

# # tuple (1, ) - 최소 하나의 값과 콤마가 필요
# # List와의 차이: 한번 만들어지면 변경 불가능.
# # 다양한 기능이 없기에 처리 속도가 빠름. list는 많은 기능이 있기 때문에 처리 속도 느림.
# # 안바꾸겠다는 의지의 표현! 안정성이 보장됨.
# print("tuple")
# tuple_a=(1,2,3)
# print(tuple_a)
# print(type(tuple_a))
# tuple_a.append(4) # append 코드 없기에 에러 발생.

# # dict (map): {}
# # key & value: 사전을 생각해라! key는 주소, value는 뜻(값)!
# dict_a={
#     "apple" : "a type of fruits",
#     "pen" : "a thing to write"
# }
# print(dict_a)
# print(dict_a["apple"])
# # edit value
# dict_a["pen"] = "something to write"
# print(dict_a)


# set set([]) : 집합
set_a=set([1,2,3,3,3,3,3,2]) # 3과 2는 중복으로 하나만 표기됨.
set_b=set([2,4,6])
print(set_a)
print(set_b)
# 집합 - 교집합, 합집합, 차집합, 여집합
# 중복 제거. 즉 한 집합에 중복해서 넣을 수 없다!! 이게 젤 중요.
print(set_a & set_b)  # 교집합
print(set_a | set_b)  # 합집합
print(set_a - set_b)  # 차집합
