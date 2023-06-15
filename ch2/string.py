# 파이썬 자료형
# 1. 문자열
# "",'',"""" """",''' ''', 세개짜리는 여러줄을 할때

# + : 결합
print("Python " + "is fun")

# * : 복제(곱하기)
print("Python " * 3)

print("*" * 50)
print("내 프로그램")
print("*" * 50)

# 인덱싱 (중요함) : 문자열은 인덱스 값을 가지고 있음(0부터 시작)

str = "Life is too short"
print(str[3])

# 슬라이싱 [시작위치 : 끝위치] => 끝 위치 포함하지 않음, 공백도 포함
print(str[2:6])
print(str[:6])  # 시작위치 지정하지 않은 경우 0
print(str[:])  # 위치 지정하지 않은 경우 0~끝
print(str[:-4])  # -값은 오른쪽 끝에서부터 위치를 잡는 경우 -1부터 시작

# len() : 길이 함수
print("str길이 : ", len(str))

str2 = "20230615Sunny"
# 년도, 날씨를 구별해서 변수에 담기
date = str2[:8]
weather = str2[8:]
print(date, weather)

# date변수에 담긴 값을 년-월-일
year = date[:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")

print(date, year)

print()
#주민등록번호 001205-3234567
#남자(1,3) / 여자(2,4) 출력
str3 ="001205-2234567"
no = str3[7]
if no=="1" or no=="3":
    print("남자")
elif no=="2" or no=="4":
    print("여자")

if int(no) %2 ==1:
    print("남")
else:
    print("여")

str1 = "대한민국"
for s in str1:
    print(s+"$",end="") #대$한$민$국$

# 입력받은 숫자만큼 하트 출력
# 54321
# ♥♥♥♥♥
# ♥♥♥♥
# ♥♥♥
# ♥♥
# ♥

# str1=input("숫자를 입력하세요") # 54321
# for i in range(len(str1)):
#     for j in range(int(str1[i])):
#         print("♥", end="")
#     print()
    
# 문자열 관련 함수
# count()
print("\n문자열 관련 함수")
str1 = "hobby"
print("count():원본 문자열에 포함된 특정 문자 개수 ",str1.count("b"))

#find()
str1 = "python is best choice"
print("find():찾는 문자의 시작 위치 반환",str1. find("b"))
print("find():없으면 -1",str1. find("k"))
print("find('i',10):10자리 위치부터 찾아줘",str1. find("i",10))
print("find('i',10):뒤에서부터 찾아줘",str1. rfind("i"))

# index() : find와 하는일 같지만 못찾는 경우 ValueError 발생
print("index():찾는 문자의 시작 위치 반환",str1.index("b"))
# print("index():없으면 -1",str1.index("k"))

#startswith() / endswith() : 특정 문자열로 시작하는지/끝나는지 (true/false)
print(str1.startswith("p"))
print(str1.endswith("p"))

# join 
str2=","
print("문자열 삽입 : ", str2.join("abced"))

# upper(), lower() : 대문자/소문자 로 변경
print("abcdef".upper())
print("ABCDEF".lower())

# swapcase() : 대소문자 서로 변경
str1 = "Python is Easy"
print(str1.swapcase())

#공백 제거 : 왼쪽, 오른쪽, 양쪽 
str1 = "        hi"
print(str1)
print("왼쪽 공백 제거", str1.lstrip())
str1 = "hi        "
print(str1)
print("오른쪽 공백 제거", str1.rstrip())
str1 = "          hi        "
print(str1)
print("양쪽 공백 제거", str1.strip())

# replace()
str1="Life is too short"
print("특정 문자열 변경", str1.replace("Life","Your leg"))

#split() =>[](리스트)로 반환
print(str1.split())  #['Life', 'is', 'too', 'short']

a="abcd"
print(a.split()) #['abcd']

a="a:b:c:d"
print(a.split(":")) #['a', 'b', 'c', 'd']

a="하나\n둘\n셋"
print(a.splitlines()) #['하나', '둘', '셋']
print(a.split()) #['하나', '둘', '셋']

# 문자열 구성 파악 - isdigit(), isalpha(), isalnum(), islower(), isupper()
print("12345".isdigit()) #숫자로만 구성되어 있니?
print("12345".isalpha()) #알파벳으로만 구성되어 있니?
print("12345".isalnum()) #알파벳 or 숫자로 구성되어 있니?

#사이트별 비밀번호를 만들어주는 프로그램
# https://www.naver.com
# 규칙1 : https://www. 제외 ==> naver.com
# 규칙2 : 처음 나오는 . 이후 부분 제외 ==> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자개수 + 글자내 e 개수 +! 구성
# 완성된 비밀번호 : nav51!
url="https://www.naver.com"
pw=0
r0=url[12:] #url=url.replace("https://www.","")
print("r0 :",r0)
r1=r0.find(".")
print("r1:",r1)
r2=r0[:r1]
print("r2:",r2)
r23=r2[:3]
print("r23:",r23)
r3=r2.count("e")
print("r3:",r3)
pw=("{}{}{}!".format(r23,r1,r3))
print("pw:",pw)

url1="https://www.naver.com"
url=url1[:url1.find(".")]
password = url[:3]+str(len(url))+str(url.count("e"))+"!"
print(password)