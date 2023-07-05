# 파일 입출력

# 파일 출력
# f = open("파일경로", "모드")
# 파일관련 작업
# ....
# 종료
# f.close

# resource 폴더에 test1.txt파일 생성
# w:write(새로작성)
# f = open("resource/test1.txt", "w")
# f.write("hello Python")
# f.close()'

# with as 구문으로 가면 close()명시하지 않아도 됨
with open("resource/test1.txt","w") as f:
    f.write("hello Python")

# f = open("resource/test1.txt", "w",encoding="utf-8")
# f.write("안녕하세요\n반갑습니다")
# f.close()

#1~10 파일에 작성
# f = open("resource/test1.txt", "w",encoding="utf-8")
# for i in range(1,11):
#     data="%d번\n" %i
#     f.write(data)
# f.close()

#a(append)
#안녕하세요 
# f = open("resource/test1.txt", "a",encoding="utf-8")
# for i in range(1,11):
#     data="안녕하세요\n"
#     f.write(data)
# f.close()

# list1 = ["홍길동","김길동","최길동"]
# #test2.txt에 리스트 안의 문자 작성
# f=open("resource/test2.txt","w",encoding="utf-8")
# for i in list1:
#     f.write(i+"\n")
# f.close()


# list1 = ["홍길동\n","김길동\n","최길동\n"]
# #test2.txt에 리스트 안의 문자 작성
# f=open("resource/test2.txt","w",encoding="utf-8")
# f.writelines(list1)
# f.close()

# dict1 = {"name":"홍길동","age":25,"addr":"서울"}
#test3.txt
# name : 홍길동
#age : 25
#사는곳 :서울
# f=open("resouce/test3.txt","w",encoding="utf-8")
# for k,v in dict1.items():
#     f.write("{}:{}\n".format(k,v))
# f.close()

import random

hanguls=list("가나다라마바사아자차카타파하")
# print(hanguls)
# print(random.choice(hanguls))
f=open("resource/info.txt","w",encoding="utf-8")
for i in range(1000):
    name=random.choice(hanguls)+random.choice(hanguls)
    weight = random.randrange(40,100)
    height = random.randrange(140,190)
    f.write("{},{},{}\n".format(name, weight, height))
f.close()
