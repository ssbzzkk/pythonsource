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
