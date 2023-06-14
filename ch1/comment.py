# 주석
"""
여러줄 주석
"""
'''
여러줄 주석
'''

#화면출력 - print() /type()
print("hello python!!")
print("100")
print(25.3)
print(type(100))  #<class 'int'>
print(type("100"))  #<class 'str'>
print(type(100.15))  #<class 'float'>
print(type(True))  #<class 'bool'>

#sep : 문자열 사이 구분자 (기본값 spacebar)
print('t','e','s','t') #t e s t
print('t','e','s','t',sep='')
print('t','e','s','t',sep='-') #t-e-s-t

#end : 기본값은 엔터, 
print('welcome To',end='')
print("the black prade")

#format : %s(문자열,정수,실수 만능), %d(정수), %f(실수), %c(문자열 하나)
print("%d" % 100)
print("%5d" % 100) #5자리 맞춰서 출력
print("%05d" % 100) #5자리 맞춰서 출력 (자릿수 없는 것은 0을 채워서)
print("%s" % "hi")
print("%5s" % "hi")
print("%-8.2f"%123.21) # - 붙이면 왼쪽 정렬, 전체자리수 8자리, 소수점 2자리
print("%8.2f"%123.21)
print("%2.5f"%1234.213456789)

#변수 선언(타입 선언 안함 : 값에 따라 타입 결정)
number =-3.32
print("i eat %d apples" % number)
print("i eat", number, "apples")

print("%d:%s"% (1,"홍길동"))
print("%s:%s"% (1,"홍길동"))

print("i eat %s apples" % 2)
print("i eat %s apples" % 2.123)
print("i eat %s apples" % "two")

#98%
print("Error is %d%%" %98)

#format() 함수
print("\nformat함수 : {}")
print("{} and {}".format("you","Me"))
print("i eat {} apples".format(3))
print("i eat {0} apples".format(3))
print("{0} and {1} and {0}".format("you","Me"))
print("{var1} and {var2}".format(var1="you",var2="Me"))
print("{0} and {var2}".format("you",var2="Me"))

#이스케이프 문자 \n, \t
print("\n줄바꿈\n연습")
print("\\ 역슬래쉬")
print(r"\n\t\\그대로 출력")
print("글자가 '강조'되는 효과 ") # 문자 표현시 "",''혀용
print('글자가 "강조"되는 효과 ') # 문자 표현시 "",''혀용
