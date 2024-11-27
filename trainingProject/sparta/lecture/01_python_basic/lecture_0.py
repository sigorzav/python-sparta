class Student:
    # 초기화 메서드
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.age = age    # 인스턴스 변수

    # 내장함수 (str: 사용자 친화적)
    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"      
        
    # 내장함수 (repr: 개발자 디버깅, 로깅 유용)
    def __repr__(self):
        return f"Student('{self.name}', {self.age})"
        
    # 내장함수 (add: 객체간의 연산 가능)
    def __add__(self, other):
        return f"{self.name + other.name}, {self.age + other.age}"

    # 메서드
    def intro(self):
        return f"{self.name} is {self.age} years old"

    # 메서드
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

# 인스턴스 생성
student = Student("Sparta", 30)

# 인스턴스 호출
print(student.intro())
print(student.speak("Hello"))

student1 = Student("Sparta1", 30)
student2 = Student("Sparta2", 31)
print(student1 + student2)