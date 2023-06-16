# 주차장 프로그램

# 메뉴제공
# [1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :

# 주차장 리스트 생성
parking_lot = []

# 주차위치, 자동차명 변수 생성
top, car_name = 0, "A"

while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료:"))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("{}자동차 들어감. 주차장 상태 ==>{}".format(car_name, parking_lot))
                top += 1
                car_name = chr(ord(car_name) + 1)
            pass
        elif no == 2:
            if top > 0:
                out = parking_lot.pop()
                print("{}자동차 나감. 주차장 상태 ==>{}".format(out, parking_lot))
                top -= 1
                car_name = chr(ord(car_name) - 1)
            else:
                print("빠져나갈 자동차가 없음")
            pass
        elif no == 3:
            break
    else:
        print("번호를 확인해 주세요")

# print(ord("A"))  # 65
# print(chr(65))  # "A"
