import random
import time
import sqlite3
from datetimes

words = []

# 시도횟수, 정답 개수
n, cor_cnt = 1, 0

# with 구문 word.txt 읽어서 words리스트에 추가
# words 출력
# ['policy','number',...]

with open("resource/word.txt") as f:
    for w in f:
        words.append(w.strip())

# print(words)

input("Redey? Press Enter Key")
start = time.time()  # 시작시간

# question 1
# read
# 사용자 입력
# 문제와 사용자 입력 일치하는지 확인
# Pass!! or Wrong!! 출력
# n증가
while n <= 5:
    # 리스트 요소 임의로 섞기
    random.shuffle(words)
    # 리스트 요소 중 임의로 하나 추출
    q = random.choice(words)
    # 추출된 요소 화면에 출력하기
    print("Question #{}".format(n))
    print(q)
    x = input()
    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt = +1  # 정답개수 추가
    else:
        print("wrong!")

    n += 1  # 문제 개수 추가

# 끝난시간
end = time.time()
# 걸린시간
et = end - start
et = format(et, ".3f")
# 게임시간, 정답개수 출력 : 게임시간 3초, 정답개수 4
print("걸린시간 {}초, 정답개수{}".format(et, cor_cnt))

# 정답 개수가 4개 이상이면 합격 출력, 불합격
if cor_cnt >= 4:
    print("합격")
else:
    print("불합격")

# db에 저장
# 테이블 records생성 : 정답개수(cor_cnt), 기록(record), 날짜(regdate, 현재날짜와 시간)
conn = sqlite3.connect("/source/pythonsource/resource/test.db", isolation_level=None)
cursor = conn.cursor()
cursor.execute(
    "create table if not exists records(cor)_cnt integer, record text, regdate text)"
)
# insert작업
now = datetime.now() #모듈명.클래스명.메소드명
nowDateTime=now.strftime("%Y-%m-%d %H:%M:%S")
cursor.execute(
    "insert into records(cor_cnt, record, regdate) values(?,?,?)",
    (cor_cnt,et,nowDateTime),
)