# 클래스 더 나아가기

class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}','{self.age}')"

sparta = human("스파르타", 30)

print(sparta.name)
print(sparta.age)

# repr 객체의 공식적인 문자열을 반환하는 메소드
print(repr(sparta))

class human2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}' __repr__ '{self.age}')"
    
    def __str__(self):
        return f"Person('{self.name}' __str__ '{self.age}')"
    
    def __add__(self, other):
        print(self.name + other.name)
        print(self.age + other.age)

    def __eq__(self, other):
        if self.name == other.name:
            print("같은 이름입니다.")
        else:
            print("다른 이름입니다.")

sparta2 = human2("스파르타2", 30)
sparta3 = human2("스파르타3", 31)

# repr을 쓸때와 안쓸때 결과가 똑같음 뭔지 알아보자
print(repr(sparta2))
print(str(sparta2))
print(sparta2)

# 객체간의 연산
sparta2 + sparta3

sparta2 == sparta3

