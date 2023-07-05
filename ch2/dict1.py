# 파이썬 자료형
# 4. 딕셔너리 (자바의 Map 동일 : key, value), key는 pk개념 , 중복되면 안됨
# {} 사용

# key값은 str, int가능
# value 값은 str, int, list, tuple, dictionary
dict1 = {"name": "park", "age": 12}
print(dict1)

# 특정 키에 해당하는 value 출력
print(dict1["name"])
print(dict1["age"])
# print(dict1["addr"]) KeyError: 'addr'

dict2 = {0: "Hello Python", 1: "Hello Java"}
print(dict2)
print(dict2[1])

dict3 = {"arr": [1, 2, 3, 4]}
print(dict3)
print(dict3["arr"])

# 요수 추가
dict1["birth"] = "0618"
print(dict1)

dict2[2] = ["Hello spring", "Hello jsp"]
print(dict2)

dict3["rank"] = (16, 17, 18)
print(dict3)

# 각 숫자가 몇 개씩 나오는지 구한 후 딕셔너리 생성
# {1:3, 2:4, 6:1...}
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
print(numbers.count(1))

# 비어있는 dict생성
counter = {}
# counter[1]=3
for number in numbers:
    counter[number] = numbers.count(number)
print(counter)

# 요소 삭제
del dict1["birth"]
print(dict1)

# 함수
# get(키값)
print(dict1.get("name"))
print(dict1.get("addr"))  # None , dict1["addr"] keyError

# 확인할 때 확인용으로 씀
# keys() : 딕셔너리 내 키 값 가져오기
print(dict1.keys()) #dict_keys(['name', 'age'])

#values()
print(dict1.values()) #dict_values(['park', 12])

# items() : key , value 쌍으로 가져오기
print(dict1.items()) #dict_items([('name', 'park'), ('age', 12)])

#in : 키가 포함되어 있는가?
print("name"in dict1) #True
print(4 in dict2) #False

print()
my_info={"name":"kim", "age":35, "city":"seoul"}

for k in my_info.keys():
    print(k)
for v in my_info.values():
    print(v)
for k,v in my_info.items():
    print(k,v)

info={v for v in my_info.values()} #{35, 'kim', 'seoul'}
print(info)

info=[v for v in my_info.values()] #['kim', 35, 'seoul']
print(info)

info={(k,v)  for k,v in my_info.items()} #{('age', 35), ('city', 'seoul'), ('name', 'kim')}
print(info)

#딕셔너리 생성하기
#"A"=90,"B"=80,"C"=70 등급을 딕셔너리로 생성하기
dict1 = {"A":90,"B":80,"C":70 }

#B키에 해당하는 값 출력하기
print(dict1["B"])
print(dict1.get("B")) #없을수도 있으면 안정성을 위헤 .get()

#B키 값을 삭제한 후 딕셔너리 출력하기
del dict1["B"]
print(dict1)
#성인 : 10000, 청소년:7000, 아동:3000 데이터를 딕셔너리 생성
dict2={"성인":10000, "청소년":7000,"아동":3000}
#위 딕셔너리에 소아 : 0항목 추가
dict2["소아"]=0
#키 값만 출력하기
print(dict2.keys()) #dict_keys(['성인', '청소년', '아동', '소아'])
#VALUE값만 출력하기
print(dict2.values()) #dict_values([10000, 7000, 3000, 0])

#list(), tuple()
print(list(dict2.keys())) #['성인', '청소년', '아동', '소아']
print(tuple(dict2.keys())) #('성인', '청소년', '아동', '소아')

print(type(dict1)) #<class 'dict'>

#key, value 전부 지우기
dict1.clear()
print(dict1)