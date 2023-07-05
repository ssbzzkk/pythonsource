def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#모듈 함수 확인용
#__name__ 는 mod1 직접 실행하게 되면 __main__이름을 가지게 됨
#           외부에서 mod1을 실행하게 되면 mod1이름을 가지게 됨
if __name__=="__main__":
    print(add(3,4))
    print(sub(3,4))