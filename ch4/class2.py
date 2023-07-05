class Student:  # 상속이 있으면 Student()
    def __init__(self, name, number, grade, details) -> None:  # 리턴타입이 없으면 None
        """
        생성자(오버로딩 없음)
        self == 자바 this
        """
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    def __str__(self) -> str:  # f리턴타입이 스트링인
        """
        toString 역할
        """
        return "이름:{},학년:{},반:{},학생정보:{}".format(
            self.name,
            self.grade,
            self.number,
            self.details,
        )


# 객체 생성
student1 = Student("kim", 1, 1, {"gender": "male", "score1": 95, "score2": 99})
student2 = Student("pak", 1, 2, {"gender": "female", "score1": 85, "score2": 89})
student3 = Student("hong", 1, 3, {"gender": "male", "score1": 75, "score2": 79})

# 확인
print(student1)
print(student2)
print(student3)
