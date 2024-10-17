import random

random_number = random.randint(1, 10)  # 1부터 10사이의 무작위 정수 생성 후 random_number 변수에 저장

user_input = int(input("""1과 10 사이의 숫자를 하나 정했습니다.
이 숫자는 무엇일까요?
예상 숫자 : """))  # 사용자에게 입력을 받음

while random_number != user_input: #while문 뒤의 조건이 거짓일때 반복이 멈춤 >> 즉, 두 변수가 같을 때 반복을 멈춘다.
    if user_input > random_number:
        print("너무 큽니다. 다시 입력하세요!")
    elif user_input < random_number:
        print("너무 작습니다. 다시 입력하세요!")

    user_input = int(input("예상숫자: "))  # 사용자에게 다시 입력받음

print("정답입니다!")