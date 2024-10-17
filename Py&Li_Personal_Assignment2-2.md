과제 내용
목표: 사용자로부터 이름, 성별, 나이를 입력받아 출력하는 프로그램 작성

처리 조건
클래스 정의
클래스 이름: Person
멤버 변수
name: 이름을 저장하는 문자열 변수
gender: 성별을 저장하는 문자열 변수 (값은 "male" 또는 "female")
age: 나이를 저장하는 정수형 변수
생성자
__init__ 메서드를 사용하여 객체 생성 시 name, gender, age를 초기화
매개변수: name, gender, age
정보 출력 함수
display() 메서드:
name과 gender를 같은 행에 출력
age는 다음 행에 출력
입력 및 출력
사용자로부터 age, name, gender를 각각 입력받는다.
입력된 값을 바탕으로 Person 객체를 생성한다.
display() 함수를 통해 객체의 정보를 출력한다.
 

예시 입출력
사용자 입력예시)
 
나이: 28
이름: 페이커
성별: male

 

출력 예시)

이름: 페이커, 성별: male
나이: 28

 

문제 해결 과정]1) 사용자에게 이름, 성별, 나이를 입력받아서 입력된 값을 바탕으로 Person 클래스를 정의하고 display()함수를 통해 객체의 정보를 출력해야 한다.

 

2) 아래 변수들을 사용한다.

name: 이름을 저장하는 문자열 변수
gender: 성별을 저장하는 문자열 변수 (값은 "male" 또는 "female")
age: 나이를 저장하는 정수형 변수
3)__init__ 메서드를 사용하여 객체 생성 시 name, gender, age를 초기화 해야 한다. 매개변수는 name, gender, age 이다.

 

4)정보 출력 함수

display() 메서드:
name과 gender를 같은 행에 출력
age는 다음 행에 출력
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
person.display()