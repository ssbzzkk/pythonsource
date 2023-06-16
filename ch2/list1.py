# 파이썬 자료형
# 2. 리스트(자바 배열, List 같은 개념)
# []

# 리스트 생성 - 데이터는 아무거나 가능
list1 = []
list2 = ["a", 1, 3.15, True]
print(list1)
print(list2)
list3 = ["a", 1, 3.15, True, ["b", 35, 45]]
print(list3)


# 리스트 인덱싱
print(list2[0])
print(list2[2])
print(list2[-1])
print(list3[-1])
print(list3[-1][1])

# 리스트 슬라이싱
print(list2[0:2])
print(list2[0:-1])
print(list3[4:])  # [['b', 35, 45]]
print(list3[4])  # ['b', 35, 45]
print(list3[4][:2])  # ['b', 35]

list4 = [1, 2, ["a", "b", ["Life", "is"]]]
# is 만나오게 하기
print(list4[2][2][1])  # is
print(list4[-1][-1][-1])  # is

# +: 연결
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1, 2, 3, 4, 5, 6]
print(a[0] + b[1])  # 6

# * : 반복
print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 특정 요소 수정
a[1] = 7
print(a)  # [1, 7, 3]
a[2] = "Life"
print(a)  # [1, 7, 'Life']

b[1:2] = [10, 11]
print(b)  # [4, 10, 11, 6]

b[1] = [15, 16, 17]
print(b)  # [4, [15, 16, 17], 11, 6]

# 리스트 요소 삭제
del b[1]
print(b)

b[0:1] = []
print(b)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("100이상의 수 ", number)

# 273 는 3자릿수 입니다.
# 103 은 3자릿수 입니다.
# 5는 1자릿수 입니다.

for number in numbers:
    print("{}는{}자릿수 입니다".format(number, len(str(number))))


# () : 튜플
list4 = list([1, 2, 3])
print(list4)

# 리스트 함수
# append() : 리스트 뒤에 요소 추가
list4.append(5)
print(list4)
list4.append([6, 7, 8])
print(list4)


# sort() : 원본을 순서대로 정렬
print("정렬 전", numbers)
numbers.sort()  # 오름차순 정렬
print("정렬 후", numbers)

alpha = ["a", "z", "c", "b", "f"]
alpha.sort()
print("정렬 후", alpha)

alpha = ["a", "z", "A", "b", "f", "D"]  # 아스키코드 A:65, a:97
alpha.sort()
print("정렬 후", alpha)

han = ["고양이", "강아지", "원숭이"]
han.sort()
print("정렬후 ", han)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
numbers.sort(reverse=True)  # 내림차순 정렬
print("정렬후", numbers)

# reverse() : 리스트 뒤집기
han.reverse()
print("reverse후", han)

# index(찾고자하는 요소) : 요소가 존재하면 위치 반환, 못찾으면 value error
print(han[0])
print(han.index("원숭이"))

# insert(위치, 요소)
han.insert(1, "악어")
print("insert후", han)

# remove(삭제할 요소) :
# list=[1,3,3,5]=> list.remove(3) : 첫번째 찾은 3만 제거, 다지우려면 두번 remove
han.remove("고양이")
print("remove후", han)

# pop(): 리스트 요소 중 마지막 요소 꺼내기
item = han.pop()
print("pop대상", item)
print("pop 후", han)
han.pop(0)
print("pop 후", han)

# count()
a = [1, 2, 3, 1]
print("list에포함된 1의 개수", a.count(1))

# clear() : 리스트 요소 모두 삭제
a.clear()
print("clear후", a)

# 리스트가 비어있으면(없으면) False임 **
list1 = []
if list:
    print("True")
else:
    print("False")

str = ""
if list:
    print("True")
else:
    print("False")

# in :포함되어있니?
print("p" in "python")
fruits = ["사과", "딸기", "배", "자몽"]
print("사과" in fruits)
print("메론" not in fruits)

# 리스트 출력
for fruit in fruits:
    print(fruit)

# enumerate() : index부여
for fruit in enumerate(fruits):
    print(fruit)  # (0, '사과')

for idx, fruit in enumerate(fruits, start=2):
    print(idx, fruit)

# A학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 70,60,55,75,95,90,80,85,100,88
# 중간고사 점수를 리스트로 생성하고, a학급의 평균 구하기

a_class = [70, 60, 55, 75, 95, 90, 80, 85, 100, 88]
total = 0
for num in a_class:
    total += num
print("평균:%.2f" % (total / len(a_class)))

# sum()이용
print("평균:%.2f" % (sum(a_class) / len(a_class)))

# 1~20 리스트 생성 : [1,2,3,4,...]
list2 = list(range(1, 21))
print(list2)

list3 = []
for x in range(1, 101):
    list3.append(x)
print(list3)

# comprehension
list3 = [x for x in range(1, 101)]
print(list3)

list4 = ["갑", "을", "병", "정", "경"]
#'정'을 제외하고 출력
for x in list4:
    if x != "정":
        print(x)

#
list5 = [x for x in list4 if x != "정"]
print(list5)

# 1~100 숫자 중에서 홀수만 리스트로 생성
list6 = list(range(1, 101, 2))
print(list6)

list8 = []
for i in range(1, 101, 2):
    list8.append(i)
print(list8)

list7 = [x for x in range(1, 101, 2)]
print(list7)

# 아래 리스트에서 소문자만 추출해서 새로운 리스트로 생성 후 출력
list9 = ["A", "b", "c", "D", "e", "F", "G", "h"]

list10 = [x for x in list9 if ord(x) > 96]
print(list10)
list11 = [x for x in list9 if x.islower()]
print(list11)

# [1,2,3,4] ==> [2,4,6,8]
print([x * 2 for x in [1, 2, 3, 4]])

# [0,1,2,3,4]=>[0,1,4,9,16]
print([x * x for x in [0, 1, 2, 3, 4]])

#[1,2,3]
#[
# [1,2,3],
# [2,3,4],
# [3,4,5]
# ]

list1=[1,2,3]
list2=[]
for x in list1:
    list2.append([x,x+1,x+2])
print(list2)

print([[x,x+1,x+2] for x in list1])

