#반복문
#while, for

i=1
while i<11:
    print(i,end=" ")
    i+=1

print()
#짝수만 출력하기
i=2
while i<101:
    print(i,end=" ")
    i=i+2
print()

# 3단 구구단
# i++ (python 불가), i=i+1, i+=1
i=1
# while i<10:
#     print("{}*{}={}".format(3,i,3*i))
#     i+=1

#in : 포함하니?
print("in 기호")
print("y" in "python") #True
print("k" in "python") #False
print("k" not in "python") #True


# range(시작값, 종료값(필수), 증감값) : 범위 지정
print(range(5)) #range(0, 5) => 0~4
print(list(range(1,5))) # [1, 2, 3, 4] 
print(list(range(0,10,2))) #[0, 2, 4, 6, 8]
 
# for
for i in range(10):
    print(i,end=" ")
for i in range(1,101):
    print(i,end=" ")
 
print()
#사용자로부터 숫자 입력 받기/1에서 입력한 숫자까지 합계 구한 후 출력

# num=int(input("숫자 입력 : ")) 
# hap=0
# for i in range(1,num+1):
#     hap+=i
# print("1~{}합계 :{}".format(num,hap))


# sum() : 이미 함수가 있음
print(sum(range(1,11)))

#역순으로 하고싶다?
for i in range(10,-1,-1):
    print(i,end=" ")

#이중포문
print()
for i in range(5):
    for j in range(5):
        print(i+j, end=" ")
    print()

#구구단
print()

for i in range(2,10):
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j),end="\t")
    print()

# break, continue : 자바 개념과 동일
i=1
while i<10:
    if i==5:
        break
    print(i,end=" ")
    i+=1
