class Person:
    def __init__(self, name, gender, age):
        # 객체 생성 시 이름, 성별, 나이를 초기화
        self.name = name       # 이름을 저장하는 문자열 변수
        self.gender = gender   # 성별을 저장하는 문자열 변수
        self.age = age         # 나이를 저장하는 정수형 변수

    def display(self):
        # name과 gender를 같은 행에 출력
        print(f"이름: {self.name}, 성별: {self.gender}")
        # age는 다음 행에 출력
        print(f"나이: {self.age}")

# 사용자로부터 입력받기
name = input("이름: ")              # 이름 입력받음
gender = input("성별 (male 또는 female): ")  # 성별 입력받음
age = int(input("나이: "))          # 나이를 정수형으로 입력받음

# Person 객체 생성
person = Person(name, gender, age)

# 정보 출력